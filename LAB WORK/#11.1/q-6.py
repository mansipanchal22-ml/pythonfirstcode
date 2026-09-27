# Q.6: Write a Python program to open a file in binary mode. 
#- Use rb mode to read the content of a text file and display its content in binary format.

with open("sample.txt", "rb") as file:
    binary_content = file.read()
    print("Binary content:", binary_content)