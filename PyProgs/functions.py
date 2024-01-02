#Funtion Examples

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Learning functions")
    
greet("Mike", "Caleb") 

print()

def get_greet(name):
    return f"Hi {name}"

message = get_greet("Mike")
print(message)

print()

#passing a variable number of arguments
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
    
print(multiply(2,3,4,5))

print()

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



print()


def grade_calc(score):
    if score >= 80:
        print("Grade A")
    elif score >= 60 and score < 80:
        print("Grade B")
    elif score >= 50 and score < 60:
        print("Grade C")
    elif score < 50:
        print("Grade F")
    else:
        print("Invalid Figure")

marks = []


while True: 
    
    user_score = input("Enter your scores for the semester(q to quit): ")
    
    if user_score == "q":
        break

    marks.append(int(user_score))
    
if marks:  
    for mark in marks:
        print(mark)
    
    total_marks = sum(marks)
    avg_marks = total_marks / len(marks)

    print("Your average marks is", avg_marks)
    grade_calc(avg_marks)

else:
    print("No marks provided.")


