# Encapsulation
# Abstruction
# some special naming convention
# name mangling , using __name()

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price

    def make_a_call(self, Phone_number):
        print(f'calling {Phone_number}..')

    def full_name(self):
        return f'{self.brand} {self.model}'


Phone1 = Phone('Nokia', '1100', 2000)
print(Phone1.__dict__)
print(Phone1._Phone__price)  # 2000
Phone1._Phone__price = 2500
print(Phone1._Phone__price)
# _name # convention of private name
# __name__ # dunder / magic methods


# l = [2, 3, 4]
# l.sort()  # tim sort
# print(l)
