# Write a program to obtain principal amount,
#  rate of interest and time from user arsd compute simple internat.  

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

si = (principal * rate * time)/100

print("The Simple Interest is:", si)
total = principal + si
print("The total amount after interest is:", total)