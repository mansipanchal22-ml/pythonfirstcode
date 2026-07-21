#write a program in python to find the maximum num 
# from the given three numbers using a nested if statement

a=10
b=20
c=30

if a >= b:
    if a >= c:
        print("The maximum number is:", a)
    else:
        print("The maximum number is:", c)
else:
    if b >= c:
        print("the maximum number is:", b)
    else:
        print("The maximum number is:", c)
