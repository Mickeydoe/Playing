for name in ["Mike", 'Vanessa']:
    print(name)
    
    
for index in range(0,10):
    print(index)


#while loop = execute some code while some condition is true

name = input("Enter your name: ")


while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
    
print(f"Hello {name}\n")

age = int(input("How old are you?: "))

while age < 0:
    print("You cannot enter a number less than 0")
    age = int(input('How old are you: '))

print(f" You are {age} years old\n")

food = input("Enter your favorite food(q to quit): ")

while not food == "q":
    print("You like {food}")
    food = input("Enter another food you like(q to quit)")

print("Bye\n")


num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 and 10: "))

print("Your number is", num)

#iterate something a certain number of times

for greet in range(6):
    print("Hola")