#Input a single digit `n` and print a 3-digit number created as `<n(n+1)(n+2)>` 
# Example: input `7` → output `789`, Assume that input digit is in range 1-7
n = int(input("Enter a single digit (1-7): "))

# Create the 3-digit number by concatenating n, n+1, and n+2
next1 = n + 1
next2 = n + 2  
three_digit_number = f"{n}{next1}{next2}"
print("The 3-digit number is:", three_digit_number)
