#q.1 Write a recursive function to calculate the factorial of a given number.Ensure the program handles edge cases (e.g., negative inputs).

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a number: "))
print("Factorial =", factorial(num))
