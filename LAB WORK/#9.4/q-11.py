#q-11 Implement a program where super() is used in a class Manager to call the constructor of its parent class.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


obj = Manager("Mansi",50000, "IT")

print("Name:", obj.name)
print("Salary:", obj.salary)
print("Department:", obj.department)