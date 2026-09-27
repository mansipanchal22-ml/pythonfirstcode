#Q.4: Create a Python program that writes multiple lines of text to a file named notes.txt. 
# - The content should be: 
# Line 1: Python is easy to learn. 
# Line 2: It has numerous libraries. 
# Line 3: File handling is one of its features.

lines = [
    "line 1: Python is easy to learn.\n"
    "line 2: It has numerous libraries.\n"
    "line 3: file handling is one of its features .\n"
]

with open("notes.txt", "w")as file:
    file.writelines(lines)

print("Multiple lines written successfully.")
