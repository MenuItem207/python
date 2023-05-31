# Writing to a File
# To write to a file, we need to open it in write mode ('w').
# We can then use the write() method to write data to the file.

# Open a file for writing
file = open("example.txt", "w")

# Write content to the file
file.write("Hello, World!")

# We can also use the writelines() method to write a list of strings to the file.
# Open a file for writing
file = open("example.txt", "w")

# Write multiple lines to the file
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file.writelines(lines)

# Closing a File
# After reading or writing a file, it's important to close it using the close() method.

# Close the file
file.close()
