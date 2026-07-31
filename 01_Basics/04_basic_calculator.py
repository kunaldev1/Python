# basic_calculator.py

print("===== Basic Calculator =====")

# Get input from the user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation
if operator == "+":     #if loop is used
    result = num1 + num2
    print("Result:", result)

elif operator == "-":    #elif loop is used
    result = num1 - num2
    print("Result:", result)

elif operator == "*":     #elif loop is used
    result = num1 * num2
    print("Result:", result)

elif operator == "/":     #elif loop is used
    if num2 != 0:         #Nested if loop is used(it means loop inside of loop)
        result = num1 / num2
        print("Result:", result)
    else:                  #Nested loop is used 
        print("Error: Division by zero is not allowed.")

else:                       #else loop is used
    print("Invalid operator! Please use +, -, *, or /.")

# Output:
# ===== Basic Calculator =====
# Addition Operation:
# Enter first number: 15
# Enter operator (+, -, *, /): +
# Enter second number: 25
# Result: 40.0

# Enter first number: 50
# Enter operator (+, -, *, /): -
# Enter second number: 18
# Result: 32.0

# ===== Basic Calculator =====
# Enter first number: 12
# Enter operator (+, -, *, /): *
# Enter second number: 8
# Result: 96.0

# ===== Basic Calculator =====
# Enter first number: 45
# Enter operator (+, -, *, /): /
# Enter second number: 9
# Result: 5.0

# ===== Basic Calculator =====
# Enter first number: 10
# Enter operator (+, -, *, /): /
# Enter second number: 0
# Error: Division by zero is not allowed.

# ===== Basic Calculator =====
# Enter first number: 12
# Enter operator (+, -, *, /): %
# Enter second number: 5
# Invalid operator! Please use +, -, *, or /.
