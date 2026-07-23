#write a program in python to find the minimum num from 
#the given three numbers using a nested if statement.

a = 40
b = 20
c = 30
d = 50

if a <= b:
    if a <= c:
        if a <= d:
            print("The maximum number is:", a)
        else:
            print("The maximum number is:", d)
else:
    if b <= c:
        if b <= d:
            print("The maximum number is:", b)
        else:
            print("The maximum number is:", d)
    else:
        if c <= d:
            print("The maximum number is:", c)
        else:
            print("The maximum number is:", d)


