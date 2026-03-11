#  Day 6 — Multiplication Table Generator

number = int(input("Enter a Number: ")) # input number multiplication table

print(f"--- {number} Multiplication Table ---") 

for i in range(1, 11): # for loop for iteration
    print(f"{number} x {i} = {number * i}") 