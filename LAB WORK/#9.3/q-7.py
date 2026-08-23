# write a program to list all the attribute and methods of a class using the dir() function.

class Student:
    
    name = "Mansi"

    def display(self):
        return "Student details"
    
print(dir(Student))
