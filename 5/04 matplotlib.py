# Matplotlib is a library for data visualization in Python.
# It provides support for creating various types of plots,
# such as line plots, scatter plots, bar plots, and histograms.
# To use Matplotlib in a Python program, we first need to import it:
import matplotlib.pyplot as plt
import numpy as np

# Now, let's create a line plot using Matplotlib:
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

plt.plot(x, y)
plt.show()

# We can customize various aspects of the plot,
# such as the title, labels, and colors:
plt.plot(x, y, color="red")
plt.title("Square Numbers")
plt.xlabel("Number")
plt.ylabel("Square")
plt.show()
