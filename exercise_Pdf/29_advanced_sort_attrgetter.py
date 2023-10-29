# Use the attrgetter if you want to sort by attributes of an object,
import datetime
from operator import attrgetter, itemgetter


class Person(object):
    def __init__(self, name, birthday, age):
        self.name = name
        self.birthday = birthday
        self.age = age

    def __repr__(self):
        return self.name


persons = [Person("John Cena", datetime.date(1992, 9, 12), 175),
           Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
           Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]  # reusing Person class from above

persons.sort(key=attrgetter('name'))  # sort by name
print(persons)

by_birthday = attrgetter('birthday')
persons.sort(key=by_birthday)  # sort by birthday
print(persons)
