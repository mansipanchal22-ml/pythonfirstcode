#Q4. Print multiplication tables up to N numbers

n = int(input("Enter the value of N: "))

for i in range(1, n + 1):
    print("Table of", i)
    for j in range(1,11):
        print(i,"x",j,"=",i * j)
    print()