# strings can also be combined together!
name = "bob"
surname = "egg"
lastname = "last"

combined_name = name + " " + surname + " " + lastname + "(end of name)"
print(combined_name)

# ints / floats can also be added in but must first be converted
random_number = 10
random_number_as_a_str = str(
    random_number
)  # str(number) converts the number into a string

combined_name = combined_name + random_number  # update combined_name
print(combined_name)

# int("string") converts the string into an int
random_str = "5"
print(random_str)
random_str_as_int = int(random_str)
print(random_str_as_int)

# * Excercise
# create these variables: name, height, favourite food
# combine them into 1 string and print it
