#Q-7.Create a class Student with private attributes for name and marks (of three subjects).
#-Add a method to calculate and display the average.
#-Add public methods to calculate and display the grade based on marks.

class Student:

    def __init__(self, name, marks1, marks2, marks3):
        self.__name = name
        self.__marks1 = marks1
        self.__marks2 = marks2
        self.__marks3 = marks3

    # Calculate and display average
    def display_average(self):
        average = (self.__marks1 + self.__marks2 + self.__marks3) / 3
        print("Average:", average)

    # Calculate and display grade
    def display_grade(self):
        average = (self.__marks1 + self.__marks2 + self.__marks3) / 3

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        print("Grade:", grade)

s1 = Student("Mansi", 90, 80, 70)

s1.display_average()

s1.display_grade()