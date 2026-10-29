# Python Tuples

A tuple is an ordered sequence that cannot be changed after creation. Tuples are useful for grouping related values that should remain fixed.

## Create tuples

```python
point = (3, 5)
rgb = (255, 128, 0)
single_item = (42,)  # The comma makes this a tuple.
```

Parentheses are often optional, but the comma is required for a one-item tuple.

## Access and unpack

```python
point = (3, 5)
x, y = point
print(x, y)
print(point[0])
```

Unpacking assigns each item to a corresponding variable. The number of targets must match the number of values unless starred unpacking is used.

## Tuple vs. list

- Tuples are immutable; lists are mutable.
- Both preserve order and support indexing and slicing.
- A tuple can contain a mutable object, but that object's contents may still change.

## When to use tuples

Use a tuple for a fixed record, such as a coordinate or RGB color. Use a list when the collection itself needs to grow, shrink, or be updated.

## Practice

1. Create a tuple containing three favorite languages.
2. Unpack a coordinate tuple into `x` and `y`.
3. Explain why `(5)` is an integer but `(5,)` is a tuple.
4. Try changing a tuple item and describe the result.

## Next topic

Continue to [Dictionaries](../09_Dictionaries/notes.md).
