#Q.2 Implement a recursive function to calculate the nth Fibonacci number.Test the function with various inputs.

def fibonacci(n):
    if n <= 0:
        return "Invalid Input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n =  int(input("Enter n: "))
print("fibonacci =", fibonacci(n))
