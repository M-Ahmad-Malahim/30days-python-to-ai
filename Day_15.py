# Day 15 — Student Marks Analyzer

import numpy as np

# Create array of marks
marks = np.array([45, 78, 90, 66, 55])

# Calculate statistics
average = marks.mean()
highest = marks.max()
lowest = marks.min()

# Filter fail students (marks < 50)
fail_students = marks[marks < 50]

# Display results
print("Marks:", marks)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Fail Students (Marks < 50):", fail_students)