# 3. **Reduce**    
#Use `reduce()` to find the maximum number in a list without using the built-in `max()`

from functools import reduce
num = [10, 23, 43, 13, 6, 50]
max = num[0]

for num in num:
    if num in num:
        max = num

print("max number:",max)

#using reduce
max = reduce(lambda x, y: x if x > y else y, num)
