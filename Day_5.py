# Day 5 — Simple CLI Calculator

# Functions
def add(a, b): # add() → addition
    return a + b

def subtract(a, b): # subtract() → subtraction
    return a - b

def multiply(a, b): # multiply() → multiplication
    return a * b

def divide(a, b): # divide() → division
    return a / b

print("Select Operation")
print("+ addition")
print("- subtraction")
print("* multiplication")
print("/ division")

choice = input("Enter Operation(+, -, *, /): ") # User Input

num_1 = float(input("Enter First Number: ")) # Numbers Input
num_2 = float(input("Enter Second Number: ")) # Numbers Input

# If Conditions
if choice == "+":
    print("Result:", add(num_1, num_2))

elif choice == "-":
    print("Result:", subtract(num_1, num_2))    

elif choice == "*":
    print("Result:", multiply(num_1, num_2))

elif choice == "/":
    print("Result:", divide(num_1, num_2))

else:
    print("Invalid Input")