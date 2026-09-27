#q-7 Use the datetime module to display the current time in UTC and your local timezone.

from datetime import datetime, timezone

utc_time = datetime.now(timezone.utc)
local_time = datetime.now().astimezone()

print("UTC Time:", utc_time)
print("Local Time:", local_time)