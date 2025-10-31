# **Q9:** Write a program to take two inputs for day,
# month and then calculate which day of the year, the gives date is.
# For simplicity, take 30 days for all month. For example,
# if you give input as: Day3, Month2 then it should print "Day of the year: 33".  

day = int(input("Enter day: "))
month = int(input("Enter month: "))

days_in_month = 30

day_in_year = month * days_in_month + day
print(f"Day of the year: {day_in_year}")