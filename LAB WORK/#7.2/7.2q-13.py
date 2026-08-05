#Q.13 Develop a program to demonstrate the difference between local and global variables with the same name.

x = 100
def show():

    x =  50
    print("Local x =",x)

show()

print("Global x =", x)

