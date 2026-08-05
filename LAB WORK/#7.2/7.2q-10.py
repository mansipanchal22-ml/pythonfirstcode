#Q.10 Write a program where a global variable is updated inside a function to keep track of the sum of all numbers entered by the user.

total = 0

def add_number(num):
    global total
    total += num

while True:
    n = int(input("Enter number (0 to stop): "))

    if n == 0:
        break
    add_number(n)

print("Total Sum =", total)