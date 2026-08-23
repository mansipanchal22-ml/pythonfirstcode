#q-1 Create a program to demonstrate single inheritance where a class parent has a method display(), and a child class child inherits and calls this method.

class Parent:
    def display(self):
        return "this is parent class"
    
class Child(Parent):

    def show(self):
        return "this is child class"
    
obj = Child()

print(obj.display())
print(obj.show())

