#Write a short program that asks for your height in centimetres
#  and then converts your height to feet and inches. (1 feet 12 inches, 1 inch-2.54 cm)

height_in_cm = float(input("Enter your height in centimetres: "))
inches = height_in_cm / 2.54 
feet = (inches // 12)   

print(f"Your height is {feet} feet and {inches} inches.")

