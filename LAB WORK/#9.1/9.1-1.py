#Q.1 Create a class Person with attributes such as name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayDitails(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")

person1 = Person("heer", 20)
person2 = Person("riya", 21)

person1.displayDitails()
person2.displayDitails()