"""Q.3 Implement a program to:
Take a string as input.
Print the string reversed, and also print whether it is a palindrome.
"""

text = input("Enter a string: ")

reverse = text[::-1]

print("Reversed String:", reverse)

if text == reverse:
    print("It is palindrome.")
