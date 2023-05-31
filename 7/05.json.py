import json

# JSON is an important format, it allows for data like
eggs = {
    "carton1": ["egg1", "egg2", "egg3"],
    "carton2": ["egg1", "egg2", "egg3"],
}
# to be converted into strings so we can upload and store the data easily
eggsJSON = json.dumps(eggs)
print(type(eggsJSON))

# to convert it back
eggsNew = json.loads(eggsJSON)
print(type(eggsNew))

# json.dumps() is a function that takes in a python object like a list or dictionary and converts it into a string
# json.loads() is a function that takes a JSON FORMATTED string and converts it back into a python object
