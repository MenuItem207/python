# Reading and writing files
# To read or write a file in Python,
# we need to open it first using the open() function.
# The open() function takes two arguments: the file name and the mode.

# Open a file for reading
file = open("example.txt", "r")

# 'r': Read mode (default). The file is opened for reading.
# 'w': Write mode. The file is opened for writing. If the file doesn't exist, it will be created. If it exists, the previous contents will be overwritten.
# 'a': Append mode. The file is opened for appending. New data will be added to the end of the file.
# 'x': Exclusive creation mode. The file is opened for writing, but it fails if the file already exists.

# Reading a File
# Once the file is opened, we can read its contents using various methods.
# The most common method is read(), which reads the entire file as a string.

# Read the contents of the file
content = file.read()

# Print the content
print(content)

# Read the file line by line
line = file.readline()

# Print each line
while line:
    print(line)
    line = file.readline()
