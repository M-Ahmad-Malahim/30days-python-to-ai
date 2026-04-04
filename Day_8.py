# Day 8 — Word Counter Tool

# Take sentence input from user
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Count total words
total_words = len(words)

# Display result
print("\n--- Word Counter ---")
print("Sentence:", sentence)
print("Total Words:", total_words)