# Python Conditions

Conditional statements let a program choose which block of code to run based on a Boolean expression.

## if, elif, and else

```python
score = 76

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Needs improvement"

print(grade)
```

Python checks conditions from top to bottom and executes the first matching branch. Indentation defines each block.

## Combining conditions

```python
age = 22
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
else:
    print("Entry not allowed")
```

Use `and`, `or`, and `not` to combine Boolean expressions. Keep complex conditions readable.

## Truthy and falsy values

Values such as `0`, `""`, `None`, and empty collections are falsy. Most other values are truthy.

```python
name = input("Name: ").strip()
if name:
    print(f"Hello, {name}!")
else:
    print("A name is required.")
```

## Common mistakes

- Using `=` instead of `==` in a comparison.
- Forgetting the colon after `if`, `elif`, or `else`.
- Incorrect indentation.
- Writing separate `if` statements when only one branch should run.

## Practice

1. Check whether an integer is positive, negative, or zero.
2. Check whether a number is even or odd.
3. Assign a grade based on a score.
4. Validate that a username is not empty after trimming whitespace.

## Next topic

Continue to [Loops](../05_Loops/notes.md).
