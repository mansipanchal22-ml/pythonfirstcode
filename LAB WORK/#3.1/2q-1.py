#write a python program to:
#-take a number as input from user
#-use an if-else statement to check if the number is odd and print the result

num = int(input("Enter a number: "))
if num % 2 != 0:
    print(num, "is an odd number.")
else:
    print(num, "is an even number.")