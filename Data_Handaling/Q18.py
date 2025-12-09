#- **Q18:** Write a program to calculate amount payable after compund interest.  
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))
compound_interest = principal * (1 + rate / 100) ** time - principal
amount_payable = principal + compound_interest
print(f"The amount payable after compound interest is: {amount_payable}")
