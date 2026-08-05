#implememnt a python program where a UDF accepts a list of integer and return the square of each integer in a new list using a list comprehension.

def square_list(lst):
    return [i**2 for i in lst]

numbers = [1,2,3,4,5]
result = square_list(numbers)
print(result)


