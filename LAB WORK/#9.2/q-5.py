# Create a class Student with appopriate attribute attribute and methods,along with a constructor.

class Student:

    def __init__(self,name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print("Student name:", self.name)
        print("Roll No:", self.roll_no)
        print("marks:", self. marks)

    def calculte_grade(self):

        if self.marks  >= 90:
            print("Grade: A")
        elif self.marks >= 75:
            print("Grade: B")
        elif self.marks >= 50:
            print("Grade: C")
        else:
            print("Grade: D")

s1 = Student("khushi", 101, 85)

s1.display_info()
s1.calculte_grade()