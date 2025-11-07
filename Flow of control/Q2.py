#
### 2. Item Price Calculator
#A store charges ₹120 per item if you buy fewer than 10 items.  
#If you buy between 10 and 99 items, the cost is ₹100 per item.  
#If you buy 100 or more items, the cost is ₹70 per item.  
#Write a program that asks the user how many items they are buying and prints the total cost.

num_items = int(input("Enter the number of items you are buying: "))   
if num_items < 10:
    price_per_item = 120
else 10 <= num_items < 100:
    price_per_item = 100
price_per_item = 70
total_cost = num_items * price_per_item
print(f"The total cost is: ₹{total_cost}")