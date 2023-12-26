#tuples are immutable

student= ("Michael Danquah", 219, 23324753,"Computer science","mike782@ggmal.com")
print(student)

#Creating an interactive tuple

name = input("Enter your first name: ")
lname = input("Enter your last name: ")
number = input("Input your phone number: ")
age = input("How old are you: ")

person = (name, lname, number,age)

print(person)

#slincing operator and functions and methods

print(len(person))
print(person.index(number))
print(person.count(name))


#using index with tuples

#Looping through tuples

for student in person:
    print(student)