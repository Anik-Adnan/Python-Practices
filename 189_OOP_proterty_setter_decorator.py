# Encapsulation
# Abstruction
# some special naming convention
# name mangling , using __name()

# will discuss three problem in exiting
# then we will solve them using getter, setter, decorator
class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        #self._price = max(price, 0)

        # if price > 0:
        #     self._price = price
        # else:
        #     self._price = 0

        # self.complete_specification = f'{self.brand} {self.model_name} and price is {self._price}'
    @property
    def complete_specifications(self):
        return f'{self.brand} {self.model_name} and price is {self._price}'

    # geteer() , seteer()
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)

    def make_a_call(self, Phone_number):
        print(f'calling {Phone_number}..')

    def full_name(self):
        return f'{self.brand} {self.model_name}'


Phone1 = Phone('Nokia', '1100', -2000)
# print(Phone1.complete_specification) # 0

# without seteer
# Phone1._price = -5000
#
# with seteer
Phone1.price = -5000

# without property
# print(Phone1._price)
#
# with property
print(Phone1.price)

# without @property
# print(Phone1.complete_specifications())
#
# with @property
print(Phone1.complete_specifications)
