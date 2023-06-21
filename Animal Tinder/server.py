from flask import Flask, request, render_template, redirect, session
import mysql.connector  # used to connect to the MySQL server

app = Flask(__name__)

# queries the database and returns the result
def queryDB(query, doesModifyData=False):
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",  # default
        password="",  # default
        database="test",  # whatever db you created
    )
    cursor = cnx.cursor()
    cursor.execute(query)

    # used when INSERTING
    if doesModifyData:
        cnx.commit()

    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return result


@app.route("/")
def home():
    # format (id, user_id...) into {'id': id, ...}
    sqlProfiles = queryDB("SELECT * FROM user_profile;")
    formattedProfiles = []

    for profiles in sqlProfiles:
        formattedProfiles.append(
            {
                "id": profiles[0],
                "user_id": profiles[1],
                "display_name": profiles[2],
                "bio": profiles[3],
                "pfp_url": profiles[4],
            }
        )

    return render_template(
        "home.html", user=session["user"], profiles=formattedProfiles
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form["email"]
        password = request.form["password"]

        # user will either be an empty [] or [(user data)]
        user = queryDB(
            f"SELECT * FROM user WHERE email = '{email}' AND password = '{password}'",
        )

        if user:  # if user found ([(user data)])
            userData = user[0]
            session["user"] = {"id": userData[0], "email": userData[1]}
            return redirect("/")
        else:
            return "Invalid email or password"


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        email = request.form["email"]
        password = request.form["password"]
        display_name = request.form["display_name"]

        queryDB(
            f"INSERT INTO user (email, password) VALUES ('{email}', '{password}');",
            True,
        )

        # fetch user_id
        id = queryDB(f"SELECT id FROM user WHERE email = '{email}' LIMIT 1")[0][0]

        # insert user_profile, no need insert bio and pfp since they can be NULL
        queryDB(
            f"INSERT INTO user_profile (user_id, display_name) VALUES ('{id}', '{display_name}');",
            True,
        )

        return redirect("/login")


@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    # Fetch the user's data from the session
    user = session["user"]

    # If the request method is GET, render the edit profile page
    if request.method == "GET":
        return render_template("edit_profile.html", user=user)
    else:
        # If the request method is POST, update the user's profile
        display_name = request.form["display_name"]
        bio = request.form["bio"]
        pfp_url = request.form["pfp_url"]
        user_id = user["id"]

        queryDB(
            f"UPDATE user_profile SET display_name = '{display_name}', bio = '{bio}', pfp_url = '{pfp_url}' WHERE user_id = '{user_id}' LIMIT 1;",
            True,
        )

        return redirect("/")


if __name__ == "__main__":
    # used to encrypt the session data
    app.secret_key = "super secret key"

    app.run(debug=True)
