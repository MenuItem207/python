# sometimes there are multiple conditions that need to be met
# we have two kinds of 'joiners' 'or' and 'and'
# (BOOLEAN_1) or (BOOLEAN_2) returns a true if either are True / truey
# (BOOLEAN_1) and (BOOLEAN_2) returns a true ONLY IF both are True / truey

if True or True:
    print("this works!")

if True or False:
    print("this works!")

if True and False:
    print("this wont work")

if True and True:
    print("this works")

if (5 - 5) or True:
    print("will this work?")

if (True or False) and True:
    print("will this work?")

if "" and 25:
    print("hi")

# real example
name = input("what is your name: ")
age = input("what is your name: ")

# only print something IF
# 1. both name and age are not falsey ("")
# AND
# 2. name not equal to "egg"
# 3. age greater than 5
if name and age and name != "egg" and age > 5:
    print("you did it!")

# * Excercise
# 1. ask the user for a number between 1 and 10
# 2. print "You picked a valid number" if the input is between 1 and 10 and not equal to 5
