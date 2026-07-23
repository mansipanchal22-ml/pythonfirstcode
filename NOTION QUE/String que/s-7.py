'''🔴 7. Remove duplicate words

```python
"this is is a test test" → "this is a test"
```

✔ Methods: `.split()`, `.join()`, membership check

'''

sentence = "this is is a test test"
words = sentence.split()
result_words = []

for word in words:
    if word not in result_words:
        result_words.append(word)

result = " ".join(result_words)
print(result) 