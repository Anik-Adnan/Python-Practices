# instance method
class Person:
    count_instance = 0

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person('Anik', 'Adnan', 22)
p2 = Person('RAhid', 'Biswas', 52)
p3 = Person('Momotuz', 'Pervin', 40)
p4 = Person('Asif', 'Adnan', 23)
print(Person.count_instance)
