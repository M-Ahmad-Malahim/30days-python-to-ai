# Basic Calculator

number_1 = int(input("Enter First Number: "))
number_2 = int(input("Enter Second Number: "))
operation = input("Enter Operation(+,-,*,/): ")

if operation == "+":  # Condition for Addtion 
   adding = number_1 + number_2
   print(f"Adding of two Numbers is {adding}" )

elif operation == "-":   # Condition for subraction
   subtraction = number_1 - number_2
   print(f"Subtraction of two Numbers is {subtraction}")

elif operation == "*":   # Condition for multiplication
   multiplication = number_1 * number_2
   print(f"Multiplication of Two Numbers is {multiplication}")

elif operation == "/":   # Condition for division
   division = number_1 / number_2
   print(f"Division of Two Numbers is {division}")

print("Thankyou")   