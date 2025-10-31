#- **Q4:** Write a program that mads a number of seconds and prints it in form mins 
# and seconds, eg. 200 seconds are printed as 3 mina and 20 seconds. 
# (Hint. use // and to get minutes and seconds).  

seconds = int(input("Enter number of seconds: "))
minutes = seconds // 60
remaining_seconds = seconds % 60
print(f"{seconds} seconds is equal to {minutes} minutes and {remaining_seconds} seconds.")