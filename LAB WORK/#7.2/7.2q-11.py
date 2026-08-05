#Q.11 Implement a program to modify a global variable that stores a username.Use a function to update the name based on user input.

username = "mansi"

def upadate_name():
    global username
    username = input("Enter new username : ")

print("Before Update:", username)

upadate_name()
print("After Update:", username)
