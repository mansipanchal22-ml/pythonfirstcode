# Q.5: Write a Python program to append 
# "Line 4: Python supports multiple modes of file handling." to the file notes.txt.

with open("notes.txt", "a") as file:
    file.write("line 4:Python supports mutliple modes of file handling.\n")

print("Line appended succesfully.")
