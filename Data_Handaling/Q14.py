#- **Q14:** Write a program that impsuns a string and then prints it equal to member of times is length, eg. Enter string "eka".  Result ekankaeka.  

string = input("Enter a string: ")
length = len(string)
result = string * length
print(f"The resulting string is: {result}")
