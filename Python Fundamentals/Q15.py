# Read three numbers into three variables. Swap the first two variables with 
# the sums of the first & second and second & third numbers respectively.

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
c = int(input("Enter the third number (c): "))

# Swap the values as per the requirement
a, b = a + b, b + c
print("After swapping:")
print("a =", a)
print("b =", b)
print("c =", c)
