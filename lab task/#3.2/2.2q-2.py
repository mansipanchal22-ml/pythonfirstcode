#write a program in python to find the maximum num 
# from the given three numbers using a nested if statement.

a = 10
b = 20
c = 30

if a <= b:
    if a <= c:
        print("The minimum number is:", a)
    else:
        print("The minimum number is:", c)

else:
    if b <= c:
        print("The minimum number is:", b)
    else:
         print("the minimum number is:", c)