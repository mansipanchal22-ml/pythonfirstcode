#Create a class employee with a default constructor to initilize attribute and a destructor to display a farewall message  when the object is deleted.

class Employee:

    def __init__(self):
        self.name = "Mansi"
        self.employee_id = 101

    def __del__(self):
        print(f"Goodbye {self.name}! Employee object is deleted.")


emp = Employee()

print("Employee Name:", emp.name)
print("Employee ID:", emp.employee_id)

del emp