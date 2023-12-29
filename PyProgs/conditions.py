price = float(input("How much did you pay: "))


if price >= 1.00:
    tax = 0.07
    print(f"Tax is {tax}")
else:
    tax = 0
    print(f"Tax rate is {tax}")