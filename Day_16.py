# Day 16 — Data Normalization

import numpy as np

# Original data
data = np.array([10, 20, 30])

# Find min and max
min_val = data.min()
max_val = data.max()

# Apply normalization formula
normalized_data = (data - min_val) / (max_val - min_val)

# Display results
print("Original Data:", data)
print("Normalized Data:", normalized_data)