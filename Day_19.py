# Day 19 — Sales Data Analyzer

import numpy as np

# Sales data
sales = np.array([200, 500, 300, 700, 100])

# Days (for better readability)
days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]

# Calculations
total_sales = np.sum(sales)
average_sales = np.mean(sales)

best_index = np.argmax(sales)
worst_index = np.argmin(sales)

# Display results
print("Sales Data:", sales)
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)

print(f"Best Day: {days[best_index]} with sales = {sales[best_index]}")
print(f"Worst Day: {days[worst_index]} with sales = {sales[worst_index]}")

# Extra insight (intermediate touch)
above_avg_sales = sales[sales > average_sales]

print("\nDays with Above Average Sales:", above_avg_sales)