'''## 🔴 15. Toggle case manually

```python
"HeLLo" → "hEllO"
```
✔ Methods:- `.isupper()`,`.islower()`,`.lower()` / `.upper()`'''

text = "HeLLo"

result = " ".join([ch.lower() if ch.isupper() 
            else ch.upper() for ch in text])

''' for loop method 
result = ""
for char in text:
    if char.isupper():
        result += char.lower()
    else:
        result += char.upper()
'''
print(result)