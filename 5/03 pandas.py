# Pandas is a library for data manipulation and analysis in Python.
# It provides support for data frames,
# which are similar to tables in a relational database.
# To use Pandas in a Python program, we first need to import it:
import pandas as pd

# data is a dictionary of data
data = {
    "Name": ["John", "Jane", "Bob", "Alice"],
    "Age": [25, 30, 40, 35],
    "Salary": [50000, 60000, 70000, 80000],
}

# Now, let's create a Pandas data frame:
df = pd.DataFrame(data)
print(df)

# Selecting columns
print(df["Name"])
# Output: 0     John
#         1     Jane
#         2      Bob
#         3    Alice
#         Name: Name, dtype: object

# Filtering rows
print(df[df["Age"] > 30])
# Output:     Name  Age  Salary
#         2   Bob   40   70000
#         3 Alice
