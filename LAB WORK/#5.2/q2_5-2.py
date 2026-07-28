#create a tuple of 5 numbers.
#-Access the third item in the tuple.
#-Try to change the second value and observe the result(explain mutability.)

number = (10, 20, 30, 40, 50)

print("Third item:", number[4])

#try to chnge the second value
#number[1] = 25 is me error aa rahi hai kyuki tuple immutable 

#list mutable he isliye us me hum usme change kr skte hai

numbers = [10, 20, 30, 40, 50]

numbers[1] = 25

print(numbers)