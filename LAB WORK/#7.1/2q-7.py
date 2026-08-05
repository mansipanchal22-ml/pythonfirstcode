#q-2 Create a user-defined function (UDF) that calculates the factorial of a given number.

def factorial(n):
    
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
print(factorial(5))