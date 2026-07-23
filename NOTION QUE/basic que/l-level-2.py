#1. Print numbers from 1 to 100 that are **divisible by 3

for i in range(1,101):
    if i % 3 == 0:
        print(i)

#2. Print numbers from 1 to 100 that are **divisible by both 3 and 5

for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#3. Count how many numbers between 1 to 50 are **even**.

count = 0

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#4. Take a number and count how many numbers from 1 to n are **divisible by 7**.

n = int(input("Enter a number:"))
count = 0

for i in range(1, n + 1):
    if  i % 7 == 0:
        count = count + 1

print("NUmbers divisible by 7 =",count)

#5. Print all numbers between 1 to n that are **not divisible by 2**.

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 !=0:
        print(i)
