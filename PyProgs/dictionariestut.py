#Dictionaries are marked by Curly Braces
#Dictionaries make use of Key Value element pairs
#Dictionaries cannot be accessed by using Indexes
#Keys in Dictionaries are immutable

student = {
    "name" : "Mike",
    "fname" : "Bob",
    "subject" : "computer science",
    "musician" : "True",
    "intruments" : ["piano","violin","flute"],
    "bands" : ["Beatles", "Crocs"]
    
}

print(student)
print(student["name"])

colors = {
    "green" : "grun",
    "blue" : "blau",
    "Red" : "rot",
    "yellow" : "gelb"
}

print(colors)

user_color = input("Name an English color: ")
german_translation = input("Enter the German translation: ")

colors[user_color] = german_translation
print(colors)

color_translation = input("Which color do you want to translate: ")
print(f"The translation for {color_translation} is {colors[color_translation]}")


