# 1. **Basic**   
#Write a program that uses `map()` to convert a list of temperatures in Celsius `[0, 10, 20, 30, 40]` to Fahrenheit.
#Formula: `F = C * 9/5 + 32`

celsius = [0, 10, 20, 30, 40]

fahrenheit = []

for c in celsius:
    f = c * 9 / 5 + 32 
    fahrenheit.append(f)

print(fahrenheit)

#using map/lambda

celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32,celsius))

print(fahrenheit)