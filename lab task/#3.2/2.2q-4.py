#write a python program using a switch-case quivalent to:
#-take an operator ("+","-","*","/") and two numbers as input
#-perform the corresponding operation on two numbers entered by the user.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
operator = input("Enter an operator (+, -, *, /): ")

match operator:

    case "+":
        print("result =", num1 + num2)

    case "-":
        print("result =", num1 - num2)

    case "*":
        print("result =", num1 * num2)

    case "/":
        if num2 != 0:
            print("result =", num1 / num2)
        else:
            print("Division by zero is not allowed.")
        
    case _:
        print("Invalid operator!")  
