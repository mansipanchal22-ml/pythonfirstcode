#Develop a program that allows users to pass any combination of attributes for an employee using **kwargs.

def employee(**kwargs):
    
    print("Employee Details")
    print("----------------")

    for key,value in kwargs.items():
        print(key, ":", value)

employee(name="veer", age=20, salary=20000, city="Ahmedabad")

print("---------------")

employee(name="meet", department="IT", designation="Developer")
