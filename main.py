#Task 1

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input('Enter your age: ')

print("Hello,", name , surname + "! You are", age, "years old!")

#Task 2

fa = float(input("Enter temperature in Fahrenheit: "))

ce = (fa - 32) * 5/9

print("Temperature in Celsius:", ce)

#Task 3

score = float(input("Enter your score: "))

if score >= 90:
    grade = 5
elif score >= 75:
    grade = 4
elif score >= 50:
    grade = 3
else:
    grade = 2

print("Your grade is:", grade)

#Task 4

# Define variable
number1 = int(input("Enter a 1st number: "))
number2 = int(input("Enter a 2nd number: "))
# Check if the number is even or odd
if number1 % number2 == 0:
    result = "can"
else:
    result = "cannot"

# Print the result
print("The 1st number", result, "be divided by the 2nd number.")

#Task 6 (5th doesn't exists)

a = float(input("Enter the length of side 1: "))
b = float(input("Enter the length of side 2: "))
c = float(input("Enter the length of side 3: "))

# Check the type of triangle
if a + b > c and a + c > b and b + c > a:
    triangle_type = "Legal"
else:
    triangle_type = "Illegal"

# Print the type of triangle
print("The triangle is:", triangle_type)

#Task 7

# Define variables
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Invalid divider"
    else:
        result = num1 / num2
else:
    result = "Invalid operation"

# Print the result
print("Result:", result)

#Task 8

