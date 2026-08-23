#q-2- implement a program to demonstrate Multiplee Inheritance using class Teacher and Administrator i  herited by a class headmaster.

class Teacher:

    def teach(self):
        return "Teacher teaches students"
    
class Administrator:

    def manage(self):
        return "Administrator manages school"
    
class Headmaster(Teacher,Administrator):

    def lead(self):
        return "Headmaster leads the school"
    
obj = Headmaster()

print(obj.teach())
print(obj.manage())
print(obj.lead())
