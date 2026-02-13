#calculator
#allow users to choose operations
print("Select operation:")
print("1.Addition(+) ")
print("2.Subtraction(-)")
print("1.Multiplication(*)")
print("1.Division(/)")

choice = input("Enter your choice 1/2/3/4:")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == "1":
    result = num1 + num2
    print(f"{num1} + {num2} = {result:.2f}")
elif choice == "2":
    result = num1 - num2
    print(f"{num1} - {num2} = {result:.2f}")
elif choice == "3":
    result = num1 * num2
    print(f"{num1} * {num2} = {result:.2f}")
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")
    else:
         print("You can't divide by 0")
else:
    print("Invalid input! Try again")


