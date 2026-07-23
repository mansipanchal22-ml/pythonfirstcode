''' 🟡 4. Extract only digits from string
```python
"a1b2c3" → "123"
```
✔ Methods: `.isdigit()`, `.join()`
'''

s = "a1b2c3"

result = "".join(ch for ch in s if ch.isdigit())

print(result)

''' for loop method
s = "a1b2c3"

result = ""

for ch in s:
    if ch.isdigit():
        result += ch

print(result)'''