# Day 9 — Prime Number Checker

# Take input from user
number = int(input("Enter a number: "))

# Assume number is prime
is_prime = True

# Check conditions
if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

# Display result
if is_prime:
    print(number, "is a Prime Number")
else:
    print(number, "is NOT a Prime Number")