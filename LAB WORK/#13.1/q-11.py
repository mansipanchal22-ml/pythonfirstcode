#q-11 Write a program that takes a date as input and prints the day of the week for that date.

from datetime import datetime

date_input = input("Enter date (YYYY-MM-DD): ")

date_object = datetime.strptime(date_input, "%Y-%m-%d")

day = date_object.strftime("%A")

print("Day:", day)