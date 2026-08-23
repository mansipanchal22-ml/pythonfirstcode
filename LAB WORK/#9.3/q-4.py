#q-4 Create a program to demostrate Hierarchical Inheritance where a base class animal is inherited by two subclass Dog and cat,each having their specific methods.

class Animal:

    def eat(self):
        return "Animal eats food"

class Dog(Animal):
    
    def bark(self):
        return "Dog barks"
    
class Cat(Animal):

    def meow(self):
        return "Cat meows"
    
dog = Dog()
cat = Cat()

print(dog.eat())
print(dog.bark())

print(cat.eat())
print(cat.meow())