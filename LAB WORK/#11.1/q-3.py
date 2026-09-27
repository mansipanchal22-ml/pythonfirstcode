#Q.3: Write a Python program to read and print the contents of the file sample.txt line by line.

with open("sample.txt", "r")as file:
    for line in file:
        print(line, end="")