#- **Q11:** Write a program that asks a user for a number of years,
#  and then prints out the number of days, hours minutes, and seconds in that number of years.  
#How many year's ? 10  
# 20.0 years is:  
# 58.8 days   
# 87600,9 hours  
# 5256000.0 minutes  
# 115360000, seconds  

years = float(input("How many year's ? "))
days = years * 365.25
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"{years} years is:")
print(f"{days} days")
print(f"{hours} hours")
print(f"{minutes} minutes")
print(f"{seconds} seconds")

