#convert a string represanting a date(eg.,"2024-01-01") into a datetime object.
#convert a datetime object into a string in the format "YYYY-MM-DD HH:MM:SS"

from datetime import datetime

date_string = "2024-01-01"

date_object = datetime.strptime(date_string,  "%Y-%m-%d")

print("Datetime object:", date_object)

result = date_object.strftime("%Y-%m-%d %H:%M:%S")

print("String:", result)
