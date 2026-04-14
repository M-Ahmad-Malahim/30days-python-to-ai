# Day 17 — 2D Array (Matrix Basics)

import numpy as np

# Create 2D array (matrix)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Get shape (rows, columns)
rows = matrix.shape[0]
columns = matrix.shape[1]

# Display results
print("Matrix:\n", matrix)
print("Number of Rows:", rows)
print("Number of Columns:", columns)