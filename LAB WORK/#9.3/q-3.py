# q-3 Write a prppgram to demostrate Multilevel Inheritance using class hierarchy:
# -Grandparent-> parent ->Child.
# -Each class should have a method to display its role.

class Grandparent:

    def display_grandparent(self):
        return "I am Grandparent"
    
class Parent(Grandparent):

    def display_parent(self):
        return "I am  Parent"
    
class Child(Parent):

    def display_child(self):
        return "I am Child"
    
obj = Child()

print(obj.display_grandparent())
print(obj.display_parent())
print(obj.display_child())
