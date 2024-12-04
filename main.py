# Program make a simple calculator

# ADITION
def add(x, y):
    return x+y

# SUBTRACTION
def subtract(x, y):
    return x-y

# MULTIPLICATION
def multiply(x, y):
    return x*y

# DIVISION
def divide(x, y):
    return x/y

num1= int(input("enter the first number: "))
num2= int(input("enter the second number: "))

print("Sum: ", add(num1, num2))
print("Difference: ", subtract(num1, num2))
print("Product: ", multiply(num1, num2))
print("Quotient: ", divide(num1, num2))