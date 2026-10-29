# Python Basics

This section introduces the basic building blocks used in nearly every Python program.

## Learning objectives

By the end of this section, you should be able to:

- Run a Python script.
- Store values in variables.
- Read input from a user.
- display output with `print()`.
- Add comments to explain code.

## Topics and examples

### 1. Hello World

```python
print("Hello, world!")
```

Run a file from a terminal with `python 01_hello_world.py`.

### 2. Variables

Variables give names to values.

```python
name = "Kunal"
age = 18
print(name, age)
```

Use descriptive names such as `total_price` rather than vague names such as `x` when the meaning is not obvious.

### 3. User input

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

`input()` returns text. Convert it when a number is required, for example `age = int(input("Age: "))`.

### 4. Output

Use `print()` to display values. f-strings are useful for inserting values into messages:

```python
language = "Python"
print(f"I'm learning {language}.")
```

### 5. Comments

Python ignores text after `#` on a line. Use comments to explain intent, not to repeat code that is already obvious.

```python
# Convert the user's input to an integer.
quantity = int(input("Quantity: "))
```

## Practice exercises

1. Print your name and one learning goal.
2. Store two numbers in variables and print their sum.
3. Ask for a user's name and greet them with an f-string.
4. Ask for a birth year and calculate an approximate age.
5. Add a comment explaining a non-obvious step in one of your programs.

## Next step

Continue to [Python Data Types](../02_Data_Types/notes.md).
