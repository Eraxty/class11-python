### 3. Time After Given Hours
#Write a program that reads from the user:  
# an hour between 1 to 12  
#- a number of hours ahead  
#Then print the time after that many hours.  

#Example:  

#Enter hour between 1-12: 9
#How many hours ahead: 4
#Time at that time would be 1 o'clock.

current_hour = int(input("Enter hour between 1-12: "))
hours_ahead = int(input("How many hours ahead: "))
new_time = (current_hour + hours_ahead) % 12
if new_time == 0:
    new_time = 12
print(f"Time at that time would be {new_time} o'clock.")    