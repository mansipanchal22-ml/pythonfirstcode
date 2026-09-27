#q-1 write a program to display the current date and time using the datetime module.
# -print the current year,month,day,hour, minute,and second from the datetime module.
 

from datetime import datetime

now = datetime.now()

print("current Date and Time:", now)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)