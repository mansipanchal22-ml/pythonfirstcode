#Develop a program that uses getter and setter methods to validate the age of a person (e.g., age must be greater than 0).

class Person:

    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid Age")

    def get_age(self):
        return self.__age

p1 = Person()

p1.set_age(20)
print("Age:", p1.get_age())