#q-10 Write a program that checks if a given year is a leap year using the datetime module.

import calendar

year = int(input("Enter year: "))

if calendar.isleap(year):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
    