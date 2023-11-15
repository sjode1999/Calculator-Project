# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x/y
    else:
        return("Can not divide by zero")




print("User Menu")
print("1. to add ")
print("2. to subtract")
print("3. to multiply")
print("4. to divide")
print("5. to exit")

while True:
    choice = input("Enter Choice (1/2/3/4/5): ")

    if choice == '5':
        print("Thank you for using calculator!!!")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Invalid Selection, Please Try Again")
        continue

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    another_calculation = input("Would you like to make a new calculation (Y/N): ")
    if another_calculation == "N":
        break
    else:
        print("Invalid Selection")

