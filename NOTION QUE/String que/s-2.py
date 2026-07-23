'''🟡 2. Capitalize each word (without `.title()`)

```python "hello world" → "Hello World"```

✔ Methods: `.split()`, `.capitalize()`, `.join()`'''

text = "hello world"

words  = text.split()

new_words = []

for word in words:
    new_words.append(word.capitalize())

result = " ".join(new_words)

print(result)


'''text = "hello world"

result = " ".join(word.capitalize() for word in text.split())

print(result)'''