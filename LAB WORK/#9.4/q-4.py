#q-4 Create a program using polymorphism where an interface Transport has a method travel().
#-Implement it differently in classes Train and Plane.

class Transport:

    def travel(self):
        return "Transport is travelling"


class Train(Transport):

    def travel(self):
        return "Train travels on railway tracks"


class Plane(Transport):

    def travel(self):
        return "Plane travels in the air"


train = Train()
plane = Plane()

print(train.travel())
print(plane.travel())