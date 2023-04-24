# Dictionaries are another way of storing data in Python
# instead of numeric indexes, they uses keys to access the values
# you can think of them like the hdb post box, where an individual key opens only 1 box

# how to define a dictionary:
phone_book = {  # curly braces are used
    "key": "value",
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012",
}

# to access a specific value:
# print(phone_book["key"]) (prints "value")
print(phone_book["Alice"])

# to add a new key-value pair
phone_book["new_key!"] = "new value!!!!"

# to update a key-value pair
phone_book["Alice"] = "new value!!!!"

# to remove a key-value pair
del phone_book["Alice"]

# dictionary keys and values are NOT limited only to strings
random_dict = {
    1: 5,
    False: "hiii",
    "wow": "",
    "": [
        1,
        2,
        3,
        4,
    ],
    "dict in a dict": {
        "hiii": "hiii",
    },
}

print(random_dict[""][0])  # what does this print?

# for loops work here too
for key in phone_book:
    print(phone_book[key])

# * Exercise
# create a dictionary of 3 animals with their chracteristics i.e name, species, age
# add a new animal
# remove one of the animals
# use a for loop to print out each animal's names and their characteristics
