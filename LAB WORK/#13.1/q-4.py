#write a program to calculate the number of days between two dates.
#add 7 days to the current date and display the result.

from datetime import date, timedelta

date1 = date(2026, 9, 21)
date2 = data(2026, 9, 30)

difference = date2 - date1 

print("numbers of days:", difference.days)

current_date = date.today()
new_date = current_date + timedelta(days=7)

print("Current Date:", current_date)
print("Date after 7 days:", new_date)
