car = {}
car["wheels"] = 4
car["color"] = "Red"
car["model"] = "Corvette"
# Dictionary values can be accessed by their keys.
print("Little " + car["color"] + " " + car["model"] + "!")
# print out "Little Red Corvette!"

# Dictionaries can also be created in a JSON style:
car = {"wheels": 4, "color": "Red", "model": "Corvette"}
# Dictionary values can be iterated over:
for key in car:
    print(f'{key} : {car[key]}')
# wheels: 4
# color: Red
# model: Corvette
