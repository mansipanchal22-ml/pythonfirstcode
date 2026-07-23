#nested if-else
# 1. Take 3 numbers and print the largest number.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2:
    if num1 > num3:
        print(num1, "is the largest.")
    else:
        print(num3, "is the largest.")
else:
    if num2 > num3:
        print(num2, "is the largest.")
    else:
        print(num3, "is the largest.")

#2. Take a year and check whether it is a leap year.
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a Leap Year.")
        else:
            print(year, "is Not a Leap Year.")
    else:
        print(year, "is a Leap Year.")
else:
    print(year, "is Not a Leap Year.")

#3. Username and Password Check
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login Success")
    else:
        print("Wrong Password")
else:
    print("Invalid User")

#4. Check if Number is Even and Divisible by 4
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is Even")

    if num % 4 == 0:
        print("Number is divisible by 4.")
    else:
        print("Number is not divisible by 4.")
else:
    print("Number is Odd.")

4. Check if Number is Even and Divisible by 4
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is Even")

    if num % 4 == 0:
        print("Number is divisible by 4.")
    else:
        print("Number is not divisible by 4.")
else:
    print("Number is Odd.")

