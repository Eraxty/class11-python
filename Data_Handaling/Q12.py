#- **Q12:** Write a program to find a side of a right angled triangle whose two sides and an angle is given. 
# without importing math module.
side_a = float(input("Enter length of side a: "))
side_b = float(input("Enter length of side b: "))

angle = float(input("Enter the angle in degrees between side a and side b: "))

hypotenuse = side_a**2 + side_b**2
hypotenuse = hypotenuse ** 0.5  
sin = side_a / hypotenuse
cos = side_b / hypotenuse


print(f"The length of the hypotenuse is: {hypotenuse}")
print(f"Sine of the angle is: {sin}")
print(f"Cosine of the angle is: {cos}")
