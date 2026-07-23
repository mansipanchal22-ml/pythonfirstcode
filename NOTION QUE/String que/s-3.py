'''🟡 3. Remove punctuation from string
python "hello!!! world??" → "hello world"
✔ Methods: .replace() (multiple times), .isalpha(), .join()'''

text = "hello!!! world??"

text = text.replace("!", "")
text = text.replace("?", "")

letters = []

for ch in text:
    if ch.isalpha() or ch == " ":
        letters.append(ch)

result = "".join(letters)

print(result)
