# Compute simple interest and compound interest
#  based on user input for principal, rate, and time.

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
compound_interest = principal * (1 + rate / 100) ** time - principal
print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)