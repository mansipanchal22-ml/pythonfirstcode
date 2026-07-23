'''Q.1 Write a Python program that:
Uses a for loop to print numbers from 1 to 20.
Skip numbers divisible by 4 using the continue statement.
'''

for i in range(1, 21):
    if i % 4 == 0:
        continue
    print(i)
    