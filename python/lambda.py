

people = [
    {"name": "Ana", "house": "campo"},
    {"name": "Gleny", "house": "Santiago"},
    {"name": "Tomas", "house": "Jobo"}
]


#def f(person):
#    return person["name"]

# tell the sort function how to sort people
# sort all the people and look up this function
#people.sort(key=f)

#people.sort(key=lambda person: person["name"])

#people.sort()

people.sort(key=lambda person: person["name"])

print(people)