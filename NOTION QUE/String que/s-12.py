'''# 🔴 12. Find longest word

```python
"I love Python programming" → "programming"
```

✔ Methods: `.split()`, `max()`
'''

sentence = "I love Python programming"
result = max(sentence.split(), key=len)
print(result)

