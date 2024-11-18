# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Take input from the usery
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")


    else:
        print("Invalid choice! Please enter a valid option.")

    # Ask if the user wants to perform another calculation
    next_calculation = input("Do you want to do another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break
def basic_calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")

        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")

        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")

        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error! Division by zero.")

    else:
        print("Invalid Input")

basic_calculator()
import math

def scientific_calculator():
    print("Select operation:")
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")
    print("4. Logarithm")
    print("5. Exponential")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        num = float(input("Enter number: "))

        if choice == '1':
            print(f"sin({num}) = {math.sin(math.radians(num))}")

        elif choice == '2':
            print(f"cos({num}) = {math.cos(math.radians(num))}")

        elif choice == '3':
            print(f"tan({num}) = {math.tan(math.radians(num))}")

        elif choice == '4':
            if num > 0:
                print(f"log({num}) = {math.log(num)}")
            else:
                print("Error! Logarithm only defined for positive numbers.")

        elif choice == '5':
            print(f"exp({num}) = {math.exp(num)}")

    else:
        print("Invalid Input")

scientific_calculator()
def bmi_calculator():
    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in meters: "))

    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi}")

    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You are normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

bmi_calculator()
def currency_converter():
    amount = float(input("Enter amount in your currency: "))
    conversion_rate = float(input("Enter conversion rate to target currency: "))
    
    converted_amount = amount * conversion_rate
    print(f"Converted amount: {converted_amount}")

currency_converter()
