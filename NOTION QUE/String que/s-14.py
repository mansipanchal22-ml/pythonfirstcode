''' 🔴 14. Check if sentence is palindrome (ignore spaces)

```python
"nurses run" → True
```

✔ Methods:

- `.replace()`
- slicing'''

sentence = "nurses run"
cleaned = sentence.replace(" ", "")
result = cleaned == cleaned[::-1]
print(result)
