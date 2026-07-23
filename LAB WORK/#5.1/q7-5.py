''''''''''Q-7 -check if a string with "hello" and ends with "world".
-remove all non -alphabetic characters from "Data123#science!".
-Reverse the string "python".'''''''

text = "hello python world"

print(text.startswith("Hello"))
print(text.endswith("World"))

text2 = "Data123#Science!"
result = ""

for ch in text2:
    if ch.isalpha():
        result += ch


print("After Removing:", result)

word = "Python"
print("Reversed:",word[::-1])

'''

text = "Hello Python World"

print(text.startswith("Hello"))
print(text.endswith("World"))

text2 = "Data123#Science!"
result = ""

for ch in text2:
    if ch.isalpha():
        result += ch

print("After Removing:", result)

word = "Python"
print("Reversed:", word[::-1])