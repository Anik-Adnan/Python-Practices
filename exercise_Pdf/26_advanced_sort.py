# If you want to sort by attributes of items, you can use the key keyword argument:
import datetime


class Person(object):
    def __init__(self, name, birthday, age):
        self.name = name
        self.birthday = birthday
        self.age = age

    def __repr__(self):
        return self.name


l = [
    Person("Asif Adnan", datetime.date(1997, 7, 6), 23),
    Person("Anik Adnn", datetime.date(1998, 7, 28), 22),
    Person("Momotuz Begum", datetime.date(1980, 4, 14), 40)]

l.sort(key=lambda item: item.name)
print(l)  # [Anik Adnn, Asif Adnan, Momotuz Begum]

l.sort(key=lambda item: item.birthday)
print(l)  # [Momotuz Begum, Asif Adnan, Anik Adnn]

l.sort(key=lambda item: item.age)
print(l)  # [Anik Adnn, Asif Adnan, Momotuz Begum]
