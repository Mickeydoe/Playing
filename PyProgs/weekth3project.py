# The owner wants you to do some calculations on the data with these criteria's:

#     -calculate the total price average for all products

#     -create a new price list that reduces the old prices by $ 5

#     -calculate the total revenue generated from the products

#     -calculate the average daily revenue generated from the products

#     -based on the new prices, which products are less than $ 30 

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

total = sum(prices)
print(total)

print()

#total price average
total_price_avg = total / len(prices)
print(f"The total price average is {total_price_avg}")

print()
#new price list that reduces old prices by 5$
red_prices = [prices - 5 for prices in prices]
print(f"The new price list reduced by 5 is {red_prices}\n")

print()

#total revenue generated from products
total_revenue = sum(quantity * price for quantity, price in zip(last_week, prices))
print(f"The total revenue is {total_revenue}\n")

print()

#average daily revenue
avg_daily_revenue = sum(last_week) / 7
print(f"The daily average is {avg_daily_revenue}\n")

#affordable pricing
affordable_price = [product for product, price in zip(products, red_prices) if price < 30]
print(f"The products that are less than 30$ are: {affordable_price}")


