#create a program that
#    -Accepts user age as input
#    -uses nested if-else statements to categorize the user into age groups:
#-Child (0-12 years)
#-Teenager (13-19 years)
#-Adult (20-59 years)
#-senior (60 +)

age = int(input("Enter your age: "))

if age >= 0:
    if age <= 12:
        print("Child.")

    else:
        if age <= 19:
            print("Teenager.")

        else:
            if age <= 59:
                print("Adult.")

            else:
                print("Senior.")    

else:

    print("Invalid age.")