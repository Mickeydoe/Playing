print("Welcome to Asanka Hotel\n")
print("This is a tip calculator")

charge = float(input("Enter the amount you are paying: "))
print(f"The amount you are paying is {charge}")

tip_calc = 18/100 * charge
sales_tax = 7/100 * charge
total = charge + tip_calc + sales_tax

print(f"Tip = {charge}")
print(f"Sales tax = {sales_tax}")
print(f"Grand total = {total}")