#1. Check if a number is Positive, Negative, or Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

#2. Check Voting Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

#3. Check if a Number is Divisible by 5
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")

#4. Find the Greater Number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1, "is greater.")
elif num2 > num1:
    print(num2, "is greater.")
else:
    print("Both numbers are equal.")

#5. Print Grade Based on Marks
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

