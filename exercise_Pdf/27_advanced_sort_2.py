# In case of list of dicts the concept is the same:
import datetime

l = [
    {'name': 'John Cena', 'birthday': datetime.date(
        1992, 9, 12), 'height': 175},
    {'name': 'Chuck Norris', 'birthday': datetime.date(
        1990, 8, 28), 'height': 180},
    {'name': 'Jon Skeet', 'birthday': datetime.date(1991, 7, 6), 'height': 185}
]
l.sort(key=lambda item: item['name'])
print(l)  # l: [Chuck Norris, John Cena, Jon Skeet]

# l.sort(key=lambda item: item['birthday'])
# print(l)  # l: [Chuck Norris, Jon Skeet, John Cena]

# l.sort(key=lambda item: item['height'])
# print(l) # l: [John Cena, Chuck Norris, Jon Skeet]
