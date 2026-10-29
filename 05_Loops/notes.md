# Python Loops

Loops repeat a block of code. Use a `for` loop to iterate over an iterable and a `while` loop to repeat while a condition remains true.

## for loops

```python
for number in range(1, 6):
    print(number)
```

`range(1, 6)` produces 1 through 5; the stop value is excluded.

Iterate over a collection directly when possible:

```python
languages = ["Python", "Java", "C"]
for language in languages:
    print(language)
```

## while loops

```python
count = 3
while count > 0:
    print(count)
    count -= 1
print("Go!")
```

Make sure the condition can eventually become false, or the loop may never end.

## break and continue

- `break` exits the nearest loop.
- `continue` skips the rest of the current iteration and moves to the next one.

Use them when they make the control flow clearer.

## Practice

1. Print the numbers from 1 to 20.
2. Calculate the sum of the numbers from 1 to 100.
3. Print a multiplication table for a number entered by the user.
4. Keep asking for input until the user enters `quit`.

## Next topic

Continue to [Functions](../06_Functions/notes.md).
