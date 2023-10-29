# objectives
# what is class
# what is INIT method, CONSTRUCTER
# how to create an class
# what are atrribtes, instance veriable


class Person:
    def __init__(self, first_name, last_name, age):
        # instance variable
        print('init methiod / constructer get called')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person('Anik', 'Adnan', 20)
p1 = Person('Anik', 'Adnan', 20)

print(p1.first_name)
print(p1)
