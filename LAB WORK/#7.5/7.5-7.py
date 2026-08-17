'''Develop a program to sort a list of dictionaries by a specific key using the sorted() function.

'''

students = [
    {"name": "mansi", "marks": 75},
    {"name": "veer", "marks": 90},
    {"name": "joy", "marks": 65},
    {"name": "jiyash", "marks": 85}
]
result = sorted(students, key=lambda x: x["marks"])

print("sorted list:")
for student in result:
    print(student)