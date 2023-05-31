# Writing to CSV Files
# To write to a CSV file, we can use the csv.writer() function.
# First, we need to import the csv module and open the CSV file in write mode.

import csv

# Open a CSV file for writing
file = open("data.csv", "w")

# Next, we can use the csv.writer() function to create a writer object.
# Create a CSV writer
csv_writer = csv.writer(file)

# We can then use the writerow() method to write rows to the CSV file.

# Write rows to the CSV file
csv_writer.writerow(["Name", "Age", "City"])
csv_writer.writerow(["John", "25", "New York"])
csv_writer.writerow(["Jane", "30", "London"])
