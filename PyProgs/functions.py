#Funtion Examples

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Learning functions")
    
greet("Mike", "Caleb") 


def get_greet(name):
    return f"Hi {name}"

message = get_greet("Mike")
print(message)


#passing a variable number of arguments
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
    
print(multiply(2,3,4,5))


#FIZZ BUZZING
def fizz_buzz(number):
    number = int(number)
    
    if number % 3 == 0 and number % 5 == 0:
        print("fizz_buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print("No fizz, No Buzz")

number = int(input("Enter to check number: "))
(fizz_buzz(number))