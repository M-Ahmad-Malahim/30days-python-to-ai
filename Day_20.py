# Day 20 — Data Insights CLI Tool

import numpy as np

# Function to take user input and convert to NumPy array
def get_data():
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(float, user_input.split()))
    return np.array(numbers)

# Function to calculate statistics
def calculate_stats(arr):
    mean_val = arr.mean()
    max_val = arr.max()
    min_val = arr.min()
    even_numbers = arr[arr % 2 == 0]

    return mean_val, max_val, min_val, even_numbers

# Function to normalize data
def normalize_data(arr):
    min_val = arr.min()
    max_val = arr.max()
    
    # Handle edge case (avoid division by zero)
    if max_val == min_val:
        return np.zeros_like(arr)
    
    return (arr - min_val) / (max_val - min_val)

# Main program
def main():
    print("=== Data Insights CLI Tool ===")
    
    data = get_data()
    
    mean_val, max_val, min_val, even_numbers = calculate_stats(data)
    normalized = normalize_data(data)

    # Display results
    print("\n--- Results ---")
    print("Data:", data)
    print("Mean:", mean_val)
    print("Max:", max_val)
    print("Min:", min_val)
    print("Even Numbers:", even_numbers)
    print("Normalized Data:", normalized)

# Run program
if __name__ == "__main__":
    main()