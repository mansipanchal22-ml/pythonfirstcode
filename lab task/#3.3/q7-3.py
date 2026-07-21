#Write a program that- Uses a `for` loop and `range()` to iterate through numbers from 1 to 50.- Checks if each number is divisible by 2, 3, or both using nested `if-elif-else`.- Prints messages for each case (e.g., "Divisible by 2", "Divisible by 3", "Divisible by both").

for i in range(1,51):
    if i % 2 == 0:
        if i % 3 == 0:
            print(i, "-Divisible by both 2 and 3")
        else:
            print(i, "-Divisible by 2")
    elif i % 3 == 0:
        print(i, "-Divisible by 3")
    else:
        print(i, "- Not divisible by 2 or 3")
