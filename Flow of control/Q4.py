# 4. Check Closeness of Numbers
#Ask the user for two numbers. Print `Close` if the numbers 
# are within 0.001 of each other, and `Not close` otherwise.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 - num2 < 0.001 and num2 - num1 < 0.001:
    print("Close")
else:
    print("Not close")
