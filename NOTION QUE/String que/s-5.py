''' 🟡 5. Extract only alphabets
```python
"a1b2c3!" → "abc"
```

✔ Methods: `.isalpha()`, `.join()`

'''

text = "a1b2c3"

result ="".join(ch for ch in text if ch.isalpha())

print(result)