# sometimes, you only want to run code based on a condition,
# thats where if-else's come in
lunch = input("What would you like to eat?: ")
if lunch == "apple":
    print("Thats good")
else:
    print("WHY NO APPLE")

# so the syntax for an ifelse statement is
# if BOOLEAN:
#   do something (make sure to press tab, the identation is very important in python)
# else:
#   do something else

if True:
    print("this works!")

if False:
    print("this doesn't work")

# numbers can also be used to represent "falsey", any number that is 0 is considered "falsey"
if 10:
    print("this works, how?")

if 0:
    print("why is this false??")

# None is also considered "falsey"
if None:
    print("this doesn't work")

# an empty string is also considered "falsey"
if "":
    print("this doesn't work either")


# there are other values that are considered "falsey" too but these are the main ones!
# * Excercise
# identify all the false or falsey values
# 50
# ""
# -1
# 10
# "False"
# False
# " "
# 0
# None
# True
# "True"
# [] (what is this?)
