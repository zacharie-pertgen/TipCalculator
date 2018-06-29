price = 0
tax = 0
tip = 0

print("Please type the price of the meal:")
price = input(int)
print("Please type the tax amount:")
tax = input(int)
print("Please type the tip percentage:")
tip = input(int)
total = price + price * tax + (price * tip / 100)
print("Your total is: " + total)