# * make sure to run
# pip install flask mysql-connector-python

from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector  # used to connect to the MYSQWL server

# configure MYSQL
app = Flask(__name__)


def queryDB(query, doesModifyData=False):
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",  # default
        password="",  # default
        database="test2",  # whatever db you created
    )
    print(query)
    cursor = cnx.cursor()
    cursor.execute(query)

    # used when INSERTING
    if doesModifyData:
        cnx.commit()

    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return result


@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        queryDB(
            f"INSERT INTO users (username, password) VALUES ('{username}', '{password}');",
            True,
        )

        return jsonify({"message": "User registered successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        try:
            username = request.form["username"]
            password = request.form["password"]

            result = queryDB(
                f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
            )

            if result:
                return redirect(url_for("content"))  # Redirect to the content page
            else:
                return jsonify({"message": "Invalid credentials!"})
        except Exception as e:
            return jsonify({"error": str(e)})


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/content")
def content():
    return render_template("content.html")


if __name__ == "__main__":
    app.run(debug=True)
