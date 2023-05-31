# Building a Simple Website with Python

# In this lesson, we will learn how to build a simple website using Python.
# We will use the Flask framework, which is a lightweight and beginner-friendly web framework in Python.

# Step 1: Installing Flask
# run this command in your terminal: pip install flask

# Step 2: Setting up the Project
# Create a new directory for your project.
# In this directory, create a new Python file called app.py. This file will contain our Flask application.

# Step 3: Importing Flask and Creating the App
from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Step 4: Defining Routes and Views
# In Flask, routes define the URL paths of your website, and views are the functions that handle those routes. Let's create our first route and view.

# Define the home route
image = "https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcQ_-LOZl1zX5IlTMOD98c8MF6be2rbRq9IaFMfMsVtaBPNVFlqLhCTk5X7b6Tw-7LbA"


@app.route("/")
def home():
    return f"""<!DOCTYPE html>
<html>
<head>
  <title>My Website</title>
</head>
<body>
  <h1>Welcome to My Website</h1>
  <img src="{image}" alt="My Image">
</body>
</html>"""


# Step 5: Running the App
# To run the Flask app, add the following code at the end of app.py:
if __name__ == "__main__":
    app.run()

# Step 6: run:
# python app.py

# Step 7: Adding More Routes and Views
# You can add more routes and views to your website by defining additional functions with the @app.route() decorator. For example:

# Define another route and view
@app.route("/about")
def about():
    return "<h2>This is the About page.</h2>"


# Define a dynamic route and view
@app.route("/user/<username>")
def user_profile(username):
    return f"<h3>Welcome, {username}!</h3>"
