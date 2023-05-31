# Working with json files
# json is sometimes store in files (.json) and we can directly edit it

import json

# Open a JSON file for reading
file = open("data.json", "r")

# Next, we can use the json.load() function to load the contents of the file as a Python object.

# Load the contents of the JSON file
data = json.load(file)

# Print the data
print(data)
