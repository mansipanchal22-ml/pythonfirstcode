#Q.7: Write a Python program that reads a text file and counts the total number of words, characters, and lines in the file.

with open("notes.txt", "r") as file:
    lines = file.readlines()

total_lines = len(lines)
total_words = sum