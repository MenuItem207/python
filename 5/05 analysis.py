# Project: Analyzing Singapore HDB Flat Prices
# In this project, we will use NumPy, Pandas, and Matplotlib
# to analyze the "Flat prices.csv" dataset,
# which contains information about
# Housing and Development Board (HDB) flat resale prices in Singapore.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas DataFrame
df = pd.read_csv("flat_prices.csv")

# Before we can analyze the dataset,
# we need to clean and prepare the data.
# For this project, we will focus on the resale prices
# of 4-room flats in the year 2020.

# Filter the DataFrame to include only 4-room flats in 2020
df_filtered = df[(df["flat_type"] == "4 ROOM") & (df["month"].str.startswith("2020"))]

# Convert the 'resale_price' column to float
df_filtered["resale_price"] = df_filtered["resale_price"].astype(float)

# Group the data by town and calculate the average resale price
df_grouped = df_filtered.groupby("town")["resale_price"].mean().reset_index()

# Sort the data by average resale price in descending order
df_sorted = df_grouped.sort_values("resale_price", ascending=False)

# Now that we have prepared the data,
# we can visualize it using Matplotlib.
# We will create a horizontal bar chart to show the
# average resale prices of 4-room flats in each town:
# Create a horizontal bar chart
plt.barh(df_sorted["town"], df_sorted["resale_price"])

# Set the title and axis labels
plt.title("Average Resale Prices of 4-Room Flats in 2020")
plt.xlabel("Average Resale Price (SGD)")

# Show the plot
plt.show()
