### 1. Convert Centimetres to Inches
#Write a Python program that asks the user to enter a length in centimetres.  
#If the user enters a negative length, the program should print that the entry is invalid.  
#Otherwise, convert the length to inches and print the result.  
#> (Note: 1 inch = 2.54 cm)

centimetres = float(input("Enter length in centimetres: "))
if centimetres < 0:
    print("Invalid entry. Length cannot be negative.")
else:
    inches = centimetres / 2.54
    print(f"The length in inches is: {inches}")
    