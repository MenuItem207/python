# Sets are another way of storing data in python, unlike lists and dictionaries they only contain unique values (NO DUPLICATES)
# they are not as commonly used as lists and dictionaries

# define a set
new_set = {1, 2, 3, 4, 4}
print(new_set)  # notice how the second 4 disappears

# add a new value
new_set.add(5)  # what happens if we add a duplicate value?
print(new_set)

# sets are useful for performing mathematical operations like UNION and INTERSECTION
set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(set_a.union(set_b))  # combines both sets without duplicates
print(set_a.intersection(set_b))  # only keeps the values that are in both sets

# for loops can also be used with sets to iterate over the values:
for value in new_set:
    print(value)

# * Exercise
# create a set with 5 random numbers, (have a couple of duplicates)
# remove a number
# add a new number
# usea for loop to print out all the numbers in the set
