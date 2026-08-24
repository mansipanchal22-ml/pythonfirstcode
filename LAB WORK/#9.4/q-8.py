#q-8 Write a program where a parent class Vehicle has a method start().
#-Demonstrate method overriding in the child classes Bike and Car with different implementation logic.

class Vehicle:

    def start(self):
        return "Vehicle is starting"


class Bike(Vehicle):

    def start(self):
        return "Bike starts with a kick"


class Car(Vehicle):

    def start(self):
        return "Car starts with a key"


bike = Bike()
car = Car()

print(bike.start())
print(car.start())
