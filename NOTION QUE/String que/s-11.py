''' 🔴 11. Remove first and last character of each word

```python
"hello world" → "ell orl"
```

✔ Methods: `.split()`, slicing, `.join()`'''

sentence = "hello world"

result = " ".join([word[1:-1] for word in sentence.split()])
print(result)