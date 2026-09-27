#Q.6 Write a program to measure the execution time of a function using the time module.

import time 

def my_function()
    total = 0
    for i in range(1000000)
        total += i
    
start_time = time.time()

my_function()

end_time = time.time

execution_time = end_time - start_time

print("Execution Time:", "second")