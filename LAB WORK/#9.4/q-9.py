#q-9 Develop a program to showcase method overloading by implementing a class Printer with a print() method that prints either a string, an integer, or both based on the arguments provided.

class Printer:

    def print(self, *args):
        return " ".join(map(str, args))


obj = Printer()

print(obj.print("Hello"))
print(obj.print(100))
print(obj.print("Age:", 20))