#q-3 write a program to format the current date as DD-MM-YYYY and MM/DD/YYYY.
#format the current time as HH:MM:SS in both 12-hour and 24-hour formats.

from datetime import datetime

now = datetime.now()

print("DD-MM-YYYY:", now.strftime("%d-%m-%y"))
print("MM/DD/YYYY:", now.strftime("%m/%d/%Y"))

print("24-hour format:", now.strftime("%H:%M:%S"))
print("12-hour format:", now.strftime("%I:%M:%S %p"))