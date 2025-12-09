#- **Q13:** Write a program to calculate the radius of a sphere whose area (sq) is given.  

area = float(input("Enter the surface area of the sphere: "))

radius = (area / (4 * 3.14)) ** 0.5
print(f"The radius of the sphere is: {radius}")
