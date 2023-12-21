import random as rm

print("Welcome to the random number generator Application")
print("The computer is going to guess a number within a range, try and guess the number for a prize. Good luck")

while True:
    computer_guess = rm.randrange(1, 20)

    print()

    # Get user's guess as an integer
    user_guess = input("Enter your guess number: ")

    # Validate if the user entered a valid integer
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Please enter a valid integer.")
        continue

    print(f"The number you guessed is {user_guess}")

    if user_guess == computer_guess:
        print("You guessed the number correctly\n")
        print("You have won a big teddy bear")
    else:
        print("You guessed the wrong number. Try again.")
    
 