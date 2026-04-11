# Day 14 — Data Filtering Tool

import numpy as np

# Create array
arr = np.array([10, 15, 20, 25])

# Filter even numbers
even_numbers = arr[arr % 2 == 0]

# Display results
print("Original:", arr)
print("Filtered (Even Numbers):", even_numbers)