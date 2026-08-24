#q-13 Create a program to demonstrate super() in a method.
#-Define a class Base with a method display().
#-Override the method in a derived class Derived and call the base class's method using super().

class Base:

    def display(self):
        return "This is Base class"


class Derived(Base):

    def display(self):
        return super().display() + " and Derived class"


obj = Derived()

print(obj.display())