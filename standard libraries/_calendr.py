import calendar

print(calendar.calendar(2025))
print()
print("="*120)
print()



print(calendar.month(2025,6))
print()
print("="*120)
print()

is_leap =calendar.isleap(2024)
print("Is 2024 is leap year : ", is_leap)
print()
print("="*120)
print()

days_in_months = calendar.monthrange(2025,6)
print("Number of days in june are : ",days_in_months)
print()
print("="*120)
print()

for n in days_in_months:
    print(n)