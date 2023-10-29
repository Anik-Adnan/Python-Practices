# base class/ parent class
# can we derive more than one class from base class ?
# multilevel inheritence
# method overriding
# isinstance(), issubclass()
class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def make_a_call(self, Phone_number):
        print(f'calling {Phone_number}..')

    def full_name(self):
        return f'{self.brand} {self.model_name}'


class Smart_Phone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, real_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.real_camera = real_camera


class FlagShipPhone(Smart_Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, real_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, real_camera)
        self.front_camera = front_camera


# Phone1 = Phone('Nokia', '1100', 2000)
# smart_Phone = Smart_Phone('OnePlus', '5', 60000, '6-GB', '64-GB', '20MP')
smartPhon = Smart_Phone(
    'OnePlus', '5', 60000, '6-GB', '64-GB', '20MP')
one_plus = FlagShipPhone(
    'OnePlus', '5', 60000, '6-GB', '64-GB', '20MP', '13MP')
# print(one_plus.full_name())

# flag_ship_phone1= FlagShipPhone(
#     'OnePlus', '5', 60000, '6-GB', '64-GB', '20MP', '13MP')
# print(flag_ship_phone1.full_name() + f'and price is {flag_ship_phone1._price}')

# print(isinstance(smartPhon, Smart_Phone)) # True
# print(isinstance(smartPhon, FlagShipPhone)) # False
# print(isinstance(smartPhon, Phone))  # True

print(issubclass(Smart_Phone, Phone))  # True
print(issubclass(Phone, FlagShipPhone))  # False
print(issubclass(FlagShipPhone, Phone))  # True
print(issubclass(FlagShipPhone, Smart_Phone))  # True
print(issubclass(Smart_Phone, FlagShipPhone))  # False
