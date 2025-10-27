#Write a program to read today’s date (only daypart) from the user,
#  then display how many days are left in the current month.


day = int(input("Enter today's date (day only): "))
month = int(input("Enter the current month (1-12): "))
if day < 1 or day > 31 or month < 1 or month > 12:
    print("Invalid date or month entered.")
    exit()

if month in [1, 3, 5, 7, 8, 10, 12]:
    days_in_month = 31 
if month in [4, 6, 9, 11]:
    days_in_month = 30
if month == 2:
    days_in_month = 28

left = days_in_month - day
print(f"There are {left} days left in this month.")