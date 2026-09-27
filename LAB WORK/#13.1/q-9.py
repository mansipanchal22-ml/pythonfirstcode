#q-9 Create a program that takes an input number of seconds from the user and counts down to zero, displaying the time remaining.

import time

seconds = int(input("Enter number of seconds: "))

while seconds > 0:

    print("Time remaining:", seconds)

    time.sleep(1)

    seconds -= 1

print("Time's up!")