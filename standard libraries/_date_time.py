import datetime
import time

now = datetime.datetime.now()
print("current date time",now)
print()
print("="*100)
print()



specific_date = datetime.datetime(2023,12,25,10,23)
print("Specific_datetime : ",specific_date)
print()
print("*"*100)
print()

#Adding 1 day to current date and time
tommorow = now + datetime.timedelta(days=1)
print("tommorow : ",tommorow)
print()
print("="*100)
print()

#formatting dates

formatted_dates = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted dates : ",formatted_dates)
print()
print("="*100)
print()

#current time in second since epoch Epoch = jan 1 1970 00:00

current = time.time()
print("Current time (seconds since epoch) : ", current)
print()
print("="*100)
print()

current_year = current/((60*60*24*365))
print("Current year : ", current_year)
print()
print("="*100)
print()

#Pausing execution

print("Pausing for 2 seconds.....")
time.sleep(2)
print("Resumed after 2 seconds ")
print()
print("="*100)
print()




