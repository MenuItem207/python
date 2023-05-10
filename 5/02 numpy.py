# NumPy is a library for numerical computing in Python.
# It provides support for multi-dimensional arrays and matrices, as well as a range of mathematical operations that can be performed on these arrays.
# To use NumPy in a Python program, we first need to import it:
import numpy as np  # imports numpy library and gives it the name np

arr = np.array([1, 2, 3, 4, 5])  # a np.array is a special list used in numpy
print(arr)

# We can perform various mathematical operations on NumPy arrays:
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Element-wise addition
print(arr1 + arr2)  # Output: [ 7  9 11 13 15]

# Element-wise multiplication
print(arr1 * arr2)  # Output: [ 6 14 24 36 50]

# Dot product
print(np.dot(arr1, arr2))  # Output: 130
