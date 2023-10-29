# class method as a constructor

class Person:
    count_instance = 0  # class variable / class atrribute

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(',')
        return cls(first, last, age)

    @classmethod
    def count_instances(cls):
        return f'You have create {cls.count_instance} instances of {cls.__name__} class'

    @staticmethod
    def hello():
        print('Hello static method called')

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        return self.age > 18


p1 = Person('Anik', 'Adnan', 22)
p2 = Person('RAhid', 'Biswas', 52)
p3 = Person('Momotuz', 'Pervin', 40)
p4 = Person('Asif', 'Adnan', 23)

p5 = Person.from_string('Anik,Adnan,22')
print(p5.full_name())

Person.hello()
