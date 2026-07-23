''' 🟡 1. Normalize a sentence
👉 Remove extra spaces + make all lowercase
``` python "  HeLLo   WoRLD  " → "hello world" ```
✔ Methods: `.strip()`, `.lower()`, `.split()`, `.join()`'''

text = "  HeLLo  WoRLD  "

text = text.strip() #remove the space
text = text.lower() #all letters convert to lowecase
words = text.split() #string con to list and clear the extra spaces
result = " ".join(words) #list con to string 

print(result)

#text = "  HeLLo   WoRLD  "
#result = " ".join(text.strip().lower().split())
#print(result)