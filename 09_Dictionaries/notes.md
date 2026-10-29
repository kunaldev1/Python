# Python Dictionaries

A dictionary stores key-value pairs. Keys must be hashable and unique; values can be of any type.

## Create and access a dictionary

```python
student = {"name": "Kunal", "language": "Python"}
print(student["name"])
print(student.get("age", "Not provided"))
```

Use square brackets when a missing key should raise `KeyError`. Use `get()` when a default is appropriate.

## Add, update, and remove values

```python
student["age"] = 18
student["language"] = "Python 3"
student.pop("age")
```

The `in` operator checks whether a key exists:

```python
if "name" in student:
    print(student["name"])
```

## Iterate over dictionaries

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

Use `keys()`, `values()`, and `items()) when their intent improves readability.

## Common mistakes

- Trying to use a mutable value such as a list as a dictionary key.
- Assuming a missing key returns `None`; bracket lookup raises `KeyError`.
- Confusing a key lookup with searching through values.

## Practice

1. Create a dictionary describing a book.
2. Count the frequency of each character in a string.
3. Safely retrieve a key that may not exist.
4. Iterate over a dictionary and print each key-value pair.

## Next step

Continue to the [Projects](../10_Projects/README.md) section and apply these concepts.
