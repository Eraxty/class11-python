#- **Q8:** Try writing program (similar to previous one) for thive digit number it, if you input 123, the program should print 321.  

num = int(input("Enter a 3-digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10
reversed_num = (units * 100) + (tens * 10) + hundreds
print("The reversed number is:", reversed_num)
