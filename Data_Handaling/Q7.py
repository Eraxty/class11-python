#* Write a program to take a 2-digit number and then
#  print the reversed number. That is, if the input given is 25, the program should print 52.  

num = int(input("Enter a 2-digit number: "))
tens = num // 10
units = num % 10
reversed_num = (units * 10) + tens
print("The reversed number is:", reversed_num)
