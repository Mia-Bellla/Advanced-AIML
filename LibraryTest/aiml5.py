import calendar

# Show whole year
print(calendar.calendar(2025))

# Month
print(calendar.month(2025, 8))

# Check leap year
print("Is 2024 leap year?", calendar.isleap(2024))

# Weekday of a date (0=Monday, 6=Sunday)
print("Weekday of 18 Aug 2025:", calendar.weekday(2025, 8, 18))
