# base class/ parent class
class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def make_a_call(self, Phone_number):
        print(f'calling {Phone_number}..')

    def full_name(self):
        return f'{self.brand} {self.model_name}'


class Smart_Phone(Phone):  # derived class / child class
    def __init__(self, brand, model_name, price, ram, internal_memory, real_camera):
        # two ways
        # Phone.__init__(self, brand, model_name, price)  # uncommon way
        super().__init__(brand, model_name, price)  # common way

        self.ram = ram
        self.internal_memory = internal_memory
        self.real_camera = real_camera


Phone1 = Phone('Nokia', '1100', -2000)
smart_Phone = Smart_Phone('OnePlus', '5', 60000, '6-GB', '64-GB', '20MP')

print(Phone1.full_name())
print(smart_Phone.full_name() + f'and price is {smart_Phone._price}')
