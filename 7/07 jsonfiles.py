# Writing to JSON Files
# To write to a JSON file, we can use the json module.
# First, we need to import the module and open the JSON file in write mode.
import json

# Open a JSON file for writing
file = open("data.json", "w")

# Next, we can use the json.dump() function to write a Python object to the JSON file.
# Create data
data = {"name": "John", "age": 25, "city": "New York"}

# Write data to the JSON file
json.dump(data, file)
