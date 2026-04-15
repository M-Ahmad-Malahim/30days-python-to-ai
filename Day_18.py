# Day 18 — Matrix Operations

import numpy as np

# Create two matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Matrix Addition
addition = A + B

# Matrix Multiplication
multiplication = np.dot(A, B)

# Display results
print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("\nAddition (A + B):\n", addition)
print("\nMultiplication (A * B):\n", multiplication)