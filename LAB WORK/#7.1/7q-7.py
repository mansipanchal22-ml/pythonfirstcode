#implement a function that accepts an aribitrary number using *args and prints each name on a new line.
#-add functionality to check if the list is empty and display a suitable message.

def names(*args):

    if len(args) == 0:
        print("no names provided")
    else:
        for i in args:
            print(i)

#names("mansi","lalit","veer")
print("-----")
names()
