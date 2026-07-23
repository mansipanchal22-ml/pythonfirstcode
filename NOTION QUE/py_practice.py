#1. Take a number from user and print its square.

num = int(input("Enter a number: "))

square = num ** 2

print("Square =", square)

#2. Take two numbers and print Addition, Subtraction, Multiplication, Division.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)

#3. Take a number and print whether it is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

#4. Take a number and print its cube.
num = int(input("Enter a number: "))

cube = num ** 3

print("Cube =", cube)

#5. Take a number and print:
#number + 10
#number * 5
num = int(input("Enter a number: "))

print("Number + 10 =", num + 10)
print("Number * 5 =", num * 5)