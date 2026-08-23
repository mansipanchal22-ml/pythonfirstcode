# q-5 Develop a program to demonstrate Hybrid Inheritance by combining multilevel and multiple inheritance.Show how the super() function helps resolve ambiguity.

class Person:

    def display(self):
        return "I am a Person"
    
class Teacher(Person):

    def display(self):
        return super().display() + "and Teacher"
    
class Administrator(Person):

    def manage(self):
        return "I am Administrator"
    
class Headmaster(Teacher,Administrator):
    
    def show(self):
        return super().display() + " and Headmaster"
    
obj = Headmaster()

print(obj.show())
print(obj.manage())