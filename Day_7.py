# Student Score Analyzer

scores = []

# Take 5 student scores from user
for i in range(5):
    score = float(input(f"Enter score {i+1}: "))
    scores.append(score)

# Calculate average
average = sum(scores) / len(scores)

# Find max and min
maximum = max(scores)
minimum = min(scores)

# Pass/Fail check (assume pass if avg >= 50)
if average >= 50:
    result = "Pass"
else:
    result = "Fail"

# Display results
print("\n--- Student Score Analysis ---")
print("Scores:", scores)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Result:", result)