#create a program that takes a user-defined function as an argument to calculate the cube of a list of numbers.

def cube(num):
    return num ** 3

def calculate_cube(fun,numbers):
    result = []

    for i in numbers:
        result.append(fun(i))

    return result

lst1 = [2,3,4,5]

ans = calculate_cube(cube,lst1)
print(ans)
