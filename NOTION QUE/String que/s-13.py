''' 🔴 13. Count words ignoring punctuation

```python
"Hello, world! Python is great." → 5

✔ Methods: - `.replace()` OR `.isalpha()``.split()`
'''
sentence = "Hello, world! Python is great."

for p in ",.!?;:":
    sentence = sentence.replace(p, "")
    print(sentence)
    