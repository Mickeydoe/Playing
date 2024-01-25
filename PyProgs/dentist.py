print("Welcome to Dentition shop Booking page")
print("Choose desired service from list below.")

print("a. Root Canal Therapy")
print("b. Oral Hygiene Check")
print("c. Emergency Injury Treatment")
print("d. Post-Procedure Check-up")
print("e. Routine Check-ups and Consultation")

print("NB: You get a 50% disount for advanced payments")

service = input("What service would you like?: ")

if service == "a":
    print("Your bill will $250")
elif service == "b":
    print("Your bill is 50")
elif service == "c":
    print("Your bill is $100")
elif service == "d":
    print("Your bill is $150")
elif service == "e":
    print("Your bill is $75")
else:
    print("Invalid selection")   
    
print("When would you like to pay? ")
pay = input("Today? [y/n]: ")
if pay.lower() == "y" :
    total = pay * 0.5
    print(f"Your total payable is {total}")
else:
    print("You will need to pay at the counter when you arrive and done served.")
    