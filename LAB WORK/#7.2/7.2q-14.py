#Q.14 Write a function that takes a list of integers and returns the sum, maximum, and minimum values as separate results.

def calculate(lst):
    return sum(lst), max(lst), min(lst)

numbers = [10,20,30,40,50]
total, maximum, minimum = calculate(numbers)

print("Sum =", total)
print("Maximum =", maximum)
print("Minimum =", minimum)
