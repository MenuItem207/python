# tuples are another way to store data in python, unlike lists they cannot be changed (immutable)

# define a tuple
new_tuple = (1, 2, 3, 4)

# access a speicfic value
print(new_tuple[1])

# you can't add to a tuple but you can create a new tuple with added or removed values
new_new_tuple = new_tuple + (
    5,
)  # what happens if we remove the comma? do we need it for multiple numbers?

# you can "unpack" a tuple into multiple variables
x, y, z, a, b = new_new_tuple  # do we need to match the length?

# tuples are often used in functions to return multiple values (next lesson)

# * Excercise
# create a tuple of 5 random numbers
# access the third value in the tuple
# unpack the tuple into 5 variables
# createa second tuple of 3 random numbers
# concatenate the 2 tuples tgt!
