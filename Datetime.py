import time
import datetime
print("current date and time:",datetime.datetime.now())
print("Current year:",datetime.date.today().strftime("%Y"))
print("month of year:",datetime.date.today().strftime("%B"))
print("week number of the year",datetime.date.today().strftime("%W"))
print("Day number of the week:",datetime.date.today().strftime("%w"))
print("Day of year:",datetime.date.today().strftime("%j"))
print("Day of the month:",datetime.date.today().strftime("%d"))
print("Day of week:",datetime.date.today().strftime("%A"))
print("\n Using time module:")
current_time=time.localtime()
print("Today's date:",time.strftime("%Y-%m-%d",current_time))