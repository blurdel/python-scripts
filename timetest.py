from datetime import datetime


# Convert strings to date objects
def toDateObj(date_string, date_format):
    s = datetime.strptime(date_string, date_format)
    return s


format = "%Y-%m-%d %H:%M:%S"
time1 = "2023-01-30 19:33:28"
time2 = "2023-01-30 19:31:28"

timeobj1 = toDateObj(time1, format)
timeobj2 = toDateObj(time2, format)

diff = timeobj1 - timeobj2

print(f"time1: {time1}")
print(f"time2: {time2}")
print(f"diff secs: {diff.total_seconds()}")
