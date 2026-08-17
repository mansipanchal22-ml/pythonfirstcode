'''Q.1
Create a list of dictionaries to store student records such as:
students = [
    {"id": 101, "name": "Alice", "score": 85},
    {"id": 102, "name": "Bob", "score": 78},
    {"id": 103, "name": "Charlie", "score": 92}
]
'''

students = [
    {"id": 101, "name": "Alice", "score": 85},
    {"id": 102, "name": "Bob", "score": 78},
    {"id": 103, "name": "Charlie", "score": 92}
]

#-Print the name of each student using a loop.
for student in students:
      print(student["name"])

#-Print the average score of all students.
total = 0

for student in students:
    total += student["score"]

average = total / len(students)

print("Average Score:", average) 

#-Add a new student record to the list. 
students.append({"id": 104, "name": "David", "score": 88})
print("add new student:", students)

#-Update the score of a student with ID 102 to 88.
for student in students:
    if student["id"] == 102:
        student["score"] = 88

print("update score:", students)

#-Delete the record of the student named "Charlie".

for student in students:
    if student["name"] == "Charlie":
        students.remove(student)

print("delete:",students)

#-Print names of students who scored more than 80.

for student in students:
    if student["score"] > 80:
        print(student["name"])


#-Sort the list of students by score (descending).
students = students[::-1]

print(student)

#-Find the student with the highest score.
highest = students[0]

for student in students:
    if student["score"] > highest["score"]:
        highest = student

print("Highest Scorer:", highest["name"])
print("Score:", highest["score"])

#-Use a loop to create a report in this format:
#Name: Alice | Score: 85 | Grade: B
#(Add grading logic: A = 90+, B = 80–89, C = <80)

for student in students:

    if student["score"] >= 90:
        grade = "A"
    elif student["score"] >= 80:
        grade = "B"
    else:
        grade = "C"

    print("Name:", student["name"], "| Score:", student["score"], "| Grade:", grade)


#-Count how many students got each grade.

a = 0
b = 0
c = 0

for student in students:
    if student["score"] >= 90:
        a += 1
    elif student["score"] >= 80:
        b += 1
    else:
        c += 1

print("Grade A:", a)
print("Grade B:", b)
print("Grade C:", c)

#-Convert the list of dictionaries into a Pandas DataFrame.

import pandas as pd

students = [
    {"id":101,"name":"Alice","score":85},
    {"id":102,"name":"Bob","score":78},
    {"id":103,"name":"Charlie","score":92}
]

df = pd.DataFrame(students)

print(df)

#-Export the DataFrame to a CSV file.

df.to_csv("students.csv", index=False)

#-Re-import it and calculate mean, min, and max of the scores.

new_df = pd.read_csv("students.csv")

print(new_df)

print("Mean =", new_df["score"].mean())
print("Min =", new_df["score"].min())
print("Max =", new_df["score"].max())