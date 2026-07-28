#create a dictionary:
#student={"name":"Alice","age":20,"grade":"A"}
#-print the key and values
#-add a new key:"city":"Delhi"
#-update "age" to 21
#-delete the "grade" key

#print k,v
student={
    "name":"Alice",
    "age":20,
    "grade":"A"
    }

print("Keys and Values:")
for key,value in student.items():
    print(key,":",value)
#add city
student["city"] = "delhi"

#update age
student["age"] = 21

#del grade
del student["grade"]


print("\n updated dictionary:")
print(student)