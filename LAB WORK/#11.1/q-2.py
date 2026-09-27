# Q.2: Write a Python program to open an existing file in read mode and display its content. 
# - Open the file in write mode, overwrite the content, and write a new sentence "Learning file handling in Python is fun!".

#read mode only content display
with open ("sample.txt", "r")as file:
    print("existing content:",file.read())

with open("sample.txt", "w")as file:
    file.write("Learning file handling in python is fun!")

print("File overwritten succesfully.")
