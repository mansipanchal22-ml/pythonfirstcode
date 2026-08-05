#Q.12 Write a program with two functions: one to initialize a global variable and another to increment it by a user-defined value.

count = 0 

def initilize():
    global count
    count = int(input("Enter initial value: "))

def increment():
    global count
    value = int(input("Enter increment value: "))
    count += value

initilize()
increment()

print("Final Value =",count)