# raise error example
# NotImplementedError
# abstrct method

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError(
            'You have to define this method in subclasses')


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    # def sound(self):
    #     return 'ghow ghow'


class Cat(Animal):
    def __init__(self, name, breed):
        super().__str__(name)
        self.breed = breed


doggy = Dog('dog_name', 'pug')
print(doggy.sound())
