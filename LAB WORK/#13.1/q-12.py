#Q.12 Write a program that schedules a reminder at a specific time using the time.sleep() function.

import time
from datetime import datetime

reminder_time = input("Enter reminder time (HH:MM): ")

print("Reminder set for", reminder_time)

while True:

    current_time = datetime.now().strftime("%H:%M")

    if current_time == reminder_time:
        print("Reminder! Time is up.")
        break

    time.sleep(1)