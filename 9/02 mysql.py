# * make sure to run
# pip install mysql-connector-python

import mysql.connector  # used to connect to the MYSQWL server

# Replace the placeholders with your actual connection details
cnx = mysql.connector.connect(
    host="localhost",
    user="root",  # default
    password="",  # default
    database="your_database",  # whatever db you created
)

# Create a cursor object
# Once the connection is established,
# create a cursor object using the cursor() method of the connection object.
# The cursor is used to execute SQL queries.
cursor = cnx.cursor()

# write a query, execute and fetch
# learn SELECT, INSERT, WHERE and LIMIT
query = "SELECT * FROM your_table"
cursor.execute(query)
result = cursor.fetchall()

print(result)

# done
cursor.close()
cnx.close()

# it will be tedious to keep writing the steps so lets write a function
def queryDB(query):
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",  # default
        password="",  # default
        database="your_database",  # whatever db you created
    )
    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return result


# now we can just do
# result = queryDB("SOME QUERY")
