#q-12 Write a program to demonstrate issubclass() in a multilevel inheritance hierarchy where Grandparent → Parent → Child.
#-Use the function to check subclass relationships.

class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

print("Is Parent a subclass of Grandparent?", issubclass(Parent,Grandparent))

print("Is Child a subclass of Parent?", issubclass(Child,Parent))

print("Is Child a subclass of Grandparent?", issubclass(Child, Grandparent))