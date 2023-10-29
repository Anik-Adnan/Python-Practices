# instance method
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        return self.age > 18
        # if self.age > 18:
        #     return age


p1 = Person('Anik', 'Adnan', 22)
print(p1.full_name())
# same as
print(Person.full_name(p1))
print(p1.is_above_18())

# l = [1, 3, 4, 5]
# print(l.clear())
# print(list.clear(l))

# l.append(100)
# print(l)
# list.append(l, 100)
# print(l)
