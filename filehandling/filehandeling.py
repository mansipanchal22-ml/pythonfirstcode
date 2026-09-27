class Student:
    def __init__(self,filename):
        self.filename = filename

    def create_student(self):
        name = input("Enter student name: ")
        course = input("Enter Course: ")

        while True:
            try:
                marks = float(input("Eenter marks(0-100): "))
                if 0<= marks <=100:
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter marks as a number.")


        file = open(self.filename,"w")
        file.write("Name:" + name +"\n")
        file.write("Course:" + course +"\n")
        file.write("Marks:"+ str(marks) +"\n")
        file.close()

        print("Student created successfully!")

    def display_student(self):
        file = open(self.filename,"r")
        content = file.read()
        file.close()

        print(".................Student Details..........")
        print(content)


student = Student("student.txt")
student.create_student()
student.display_student()