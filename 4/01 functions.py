# sometimes, we write code that needs to be used multiple times
# functions are blocks of reusable code that perform a specific task

# define a function with the keyword def
# def function_name(parameter_1, ..., parameter_n):
# <tab>print(parameter_1)
def greet(name):
    print("Hello " + name)  # print is a function too


# you can call the funciton after defining it
greet("bob")
greet("alice")

# functions can also return values
def add(a, b):
    return a + b


final_value = add(1, 5)  # add returns a value

# function paramters can have default values!
def greet2(name, greeting="Hello "):
    print(greeting + name)


greet2("Alice")
greet2("Alice", "Bye ")

# when you define a variable inside a function, it has local SCOPE
# this means that it can also be accessed within that function (same amount of tab)
# so tabbing defines the SCOPE
def rand_func():
    x = 1
    print(x)


print(x)  # not defined

# * Exercise
# define a function that takes in a list of numbers and returns the sum of those numbers
# define a function that takes two strings and returns a string with those two strings concatenated
# define a function that takes a number and returns True if it's even, False if its odd
