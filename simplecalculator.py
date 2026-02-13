# a somple calculator in python
from random import choice

#Display options to the user
print("Select  operation :")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Division (/)")
print("4. Multiplication (*)")

#take inputs from the user
choice = input("Enter your choice(1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#perform the operation
if choice == "1" :
   result = num1 + num2
   print(f"{num1} + {num2} = {result:.2f}")
elif choice == "2" :
    result = num1 - num2
    print(f"{num1} - {num2} = {result: .2f}")
elif choice == "3" :
    result = num1 * num2
    print(f"{num1} * {num2} = {result: .2f}")

elif choice == "4" :
         if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result: .2f}")
         else:
            print("Error: Division by zero is not allowed ")

else:
    print("Invalid input! Try again")



