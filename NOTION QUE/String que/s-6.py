''' 🔴 6. Reverse words in a sentence

```python
"I love Python" → "Python love I"
```

✔ Methods: `.split()`, slicing, `.join()`
'''
sentence = "I love Python"

result = " ".join(sentence.split()[::-1])

print(result)
