#q-6 Implement a program to demonstrate method overriding where a class Animal has a method speak(), and subclasses Dog and Cat override it with their respective sounds.

class Animal:

    def speak(self):
        return "Animal makes a sound"


class Dog(Animal):

    def speak(self):
        return "Dog barks"


class Cat(Animal):

    def speak(self):
        return "Cat meows"


dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())