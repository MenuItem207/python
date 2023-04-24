# lists are a way to store multiple values in a single variable
# the position of items in the list remains constant unless the list is explicitly updated
# we define lists like this:
shopping_list = [
    "eggs",  # index 0
    "milk",  # index 1
    "cheese",  # index 2
    "chicken",  # index 3
]  # a list is created and stored in the variable shopping_list

# to view the list:
print(shopping_list)

# to access a specific item in the list
# (items in a list can be accessed by using their index which is their place in the list starting from 0)
print(shopping_list[0])

# lets add an item to the back of the list
shopping_list.append("orange juice")
print(shopping_list)

# lets combine two lists
shopping_list_2 = [
    "milo",
    "chocolates",
]
shopping_list.extend(shopping_list_2)
print(shopping_list)

# lets remove an item from the back of the list
shopping_list.pop()
print(shopping_list)

# lets remove an item from a specfic position
shopping_list.pop(1)
print(shopping_list)

# lets insert an item at a specific index
shopping_list.insert(1, "NEW ITEM AT INDEX 1")
print(shopping_list)


# * Excercise
# Create a list with 5 random names
# Remove the name at index 3
# Add a name add the start of the list
# Create a second list with 3 random numbers
# Add the 3 numbers to the first list
# print out the 7th item (which index is this?)
