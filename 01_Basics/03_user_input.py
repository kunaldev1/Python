# user_input.py

# Taking users input
print("User Input:-")
name = input("Enter your name: ")   #String Value
age = int(input("Enter your age: "))   #Integer Value
height = float(input("Enter your height: "))   #Floating Value

print("\n----- User Information -----")
print("Name:", name)
print("Age:", age)
print("Height:", height, "feet")

print("\nHello", name + "!")
print("Next year you will be", age + 1, "years old.")

# Output:
# User Input:-
# Enter your name: Kunal
# Enter your age: 17
# Enter your height: 5.7 
# -----User Information-----
# Name: Kunal
# Age: 17
# Height: 5.7 feet
# /n made a break or like a statement that skips one line.
# Hello Kunal!
# Next year you will be 18 years old.
