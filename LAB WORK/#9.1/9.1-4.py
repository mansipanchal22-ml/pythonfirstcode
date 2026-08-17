# Q-4.write a program to create a class book with private attributes title and auther.
#-add public methods to set and get these attributes.

class Book:

    def __init__(self):
        self.__title = ""
        self.__author = ""

    # Set methods
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    # Get methods
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

book1 = Book()

book1.set_title("Harry Potter")
book1.set_author("J.K.Rowling")

print("Title:", book1.get_title())
print("Author:", book1.get_author())