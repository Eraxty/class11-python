#- **Q16:** Write a program to input the radius of a sphere and calculate its volume v = 4/3 pi r3.  

radius = float(input("Enter the radius of the sphere: "))
pi = 3.14
volume = (4/3) * pi * radius**3
print(f"The volume of the sphere is: {volume}")
