# 2. **Filter + Sorted**
#Given a list of numbers `[12, 5, 8, 23, 16, 4, 42, 7]`, use 
# filter()` to keep only the even numbers,
#then use `sorted()` to sort them in descending order.

numbers = [12, 5, 8, 23, 16, 4 ,42, 7]

even_sorted = sorted(filter(lambda x: x % 2 == 0, numbers),reverse= True)

print(even_sorted)