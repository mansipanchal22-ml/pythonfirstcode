#Create a class Animal with a constuctor that initialize the name attribute.
#-add a method to display the name of the animal

class Animal:

    def __init__(self, name):
        self.name = name  

    def display_name(self):
        print("Animal Name:", self.name)

a1 = Animal("Lion")

a1.display_name()