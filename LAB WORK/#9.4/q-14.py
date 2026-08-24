#q-14 Develop a program where a class Admin inherits from User.
#-Use super() to initialize the attributes of the User class in the Admin constructor.

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Admin(User):

    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role


obj = Admin("Mansi", "mansi@gmail.com", "Administrator")

print("Name:", obj.name)
print("Email:", obj.email)
print("Role:", obj.role)