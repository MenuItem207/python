# Working with CSV Files

# Reading CSV Files
# To read a CSV file, we can use the csv module in Python.
# First, we need to import the module and open the CSV file.

import csv

# Open a CSV file for reading
file = open("data.csv", "r")

# Next, we can use the csv.reader() function to read the contents of the file as a list of rows.

# Create a CSV reader
csv_reader = csv.reader(file)

# Read the contents of the file
rows = list(csv_reader)

# Print each row
for row in rows:
    print(row)
