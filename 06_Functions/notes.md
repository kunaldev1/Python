# Python Functions

Functions package reusable behavior into named blocks. They help reduce repetition and make programs easier to test.

## Define and call a function

```python
def greet(name):
    """Return a greeting for a name."""
    return f"Hello, {name}!"

message = greet("Kunal")
print(message)
```

- Parameters are names in the function definition.
- Arguments are values supplied when calling the function.
- `return` sends a result back to the caller.
- A function without an explicit return value returns `None`.

## Default and keyword arguments

```python
def power(base, exponent=2):
    return base ** exponent

print(power(4))             # 16
print(power(2, exponent=3)) # 8
```

## Scope

Variables created inside a function are local to that function unless other mechanisms are used. Prefer passing inputs as parameters and returning results instead of relying on global state.

## Docstrings

A docstring explains a function's purpose, arguments, and return value when those details are useful. Keep it accurate and concise.

## Practice

1. Write a function that returns the larger of two numbers.
2. Write a function that converts Celsius to Fahrenheit.
3. Write a function that returns whether a number is even.
4. Write tests for a function using several normal and edge-case inputs.

## Next topic

Continue to [Lists](../07_Lists/notes.md).
