#Input a number and print its first five multiples.
number = int(input("Enter a number: "))
print("The first five multiples of", number, "are:")
for i in range(1, 6):
    print(number * i)