# **Q17:** Write a program to calculate amount payable after simple interest.  

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))
simple_interest = (principal * rate * time) / 100
amount_payable = principal + simple_interest
print(f"The amount payable after simple interest is: {amount_payable}")
