#q-1 Write a program that creaters multiple objects of a class and deletes them using the del keyword.
#- Observe the behavior(using the destructor).

class Student:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} object is deleted")


s1 = Student("Mansi")
s2 = Student("Veer")
s3 = Student("Joy")

print("Three objects are created")

del s1
del s2
del s3