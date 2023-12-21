names = ["Susan","Mike", "Daniel","Van", "Kojo"]
print(len(names))#get number of items
names.insert(0, "Sandra") #insert before index
print(names)
names.sort  
print(names)

print()
#retrieving ranges
print(names[0:4])

print()
#DICTIONARIES

Boys = {"First" : "Kofi" , "Last": "Ablao"}
print(Boys)

person1 = {}
person1['first'] = "Vanessa"
person1["last"] = "Acquah"

person2 = {}
person2['first'] = "Andy"
person2["last"] = "Kelly"

people = []
people.append(person1)
people.append(person2)
people.append({"first": "Bill", "last" : "Gates"})
print(people)