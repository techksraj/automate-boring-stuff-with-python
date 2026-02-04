import calendar
from datetime import datetime

# year = int(input('Enter the year:'))
# month = int(input('Enter the month:'))

# cal = calendar.calendar(year, month)
cal = calendar.calendar(2025, 2)
print(cal)

print(datetime(2025,1,1))
print(datetime.isoformat(datetime.now()))
print(datetime.weekday(datetime(2024,12,29)))
print(datetime.now())
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))