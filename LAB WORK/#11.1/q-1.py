# Write a Python program to create a text file named sample.txt.
#- Write the sentence "Python is a versatile programming language." into the file.

# 'w' mode create file and write data
with open("sample.txt", "w") as file:
    file.write("Python is a versatile programming language.")

print("File created and written successfully.")