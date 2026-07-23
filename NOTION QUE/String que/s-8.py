''' 🔴 8. Check if email is valid (basic)
```python
"test@gmail.com" → True
```
✔ Conditions:
- contains `"@"`
- endswith `.com`

✔ Methods: `.count()`, `.endswith()`, `.find()` '''

email = "test@gmail.com"

is_valid = email.count("@") == 1 and email.endswith(".com")
print(is_valid)
