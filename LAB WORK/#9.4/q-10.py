#q-10 Write a program to demonstrate the use of issubclass() by creating classes Person and Student (derived from Person).
#-Check if Student is a subclass of Person and print the result.

class Person:
    pass


class Student(Person):
    pass


result = issubclass(Student, Person)

print("Is Student a subclass of Person?", result)