# Write a program to obtain temperatures of 7 days (Monday, Tuesday Sunday) 
# and then display average temperature of the week.

moday_temp = float(input("Enter the temperature for Monday: "))
tuesday_temp = float(input("Enter the temperature for Tuesday: "))
wednesday_temp = float(input("Enter the temperature for Wednesday: "))
thursday_temp = float(input("Enter the temperature for Thursday: "))
friday_temp = float(input("Enter the temperature for Friday: "))
saturday_temp = float(input("Enter the temperature for Saturday: "))
sunday_temp = float(input("Enter the temperature for Sunday: "))

total_temp = (moday_temp + tuesday_temp + wednesday_temp + thursday_temp + friday_temp + saturday_temp + sunday_temp)/7
print("The average temperature of the week is:", total_temp)