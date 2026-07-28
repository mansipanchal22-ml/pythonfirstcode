#create a list of square of numbers from 1 to 10 using list comprehension.
#create a new list that only contains even numbers from given list [1,2,3,...,20]
#convert all string in a list ["hello","WORLD","PyThOn"] to lowercase uaing list comprehension.

#1
square = [i**2 for i in range(1,11)]

print(square)

#2
numbers = list(range(1,21))
even = [i for i in numbers if i % 2 == 0]
print(even)

#3
list2 = ["hello","WORLD","PyThOn"]

lower = [list2.lower() for list2 in list2]

print(lower)