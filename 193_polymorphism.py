# sepecial magic method / dunder method
# operator ovrloading n
# polymorphism /[method overriding]

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model}"
    # str , repr

    def __str__(self):
        return f"{self.brand} {self.model} price is {self.price}"

    def __repr__(self):
        return f"Phone('{self.brand}','{self.model}','{self.price}')"

    def __len__(self):
        return len(self.phone_name())

    def __add__(self, other):
        return self.price + other.price

    def __mul__(self, other):
        return self.price * other.price


class Smart_Phone(Phone):
    def __init__(self, brand, model, price, ram, real_camera):
        super().__init__(brand, model, price)
        self.ram = ram
        self.real_camera = real_camera

    def phone_name(self):
        return f'{self.brand} {self.model} {self.price}'


# l = [1, 3, 4, 5]
# print(l)
# przint(len(l))
my_phone = Phone('nokia', '1100', 2500)
my_phone2 = Phone('nokia', '1600', 3000)
smart_Phone = Smart_Phone('OnePlus', '5', 60000, '6-GB', '20MP')

print(str(my_phone))  # nokia 1100 price is 2500
print(repr(my_phone))  # Phone('nokia','1100','2500')
print(my_phone.__str__())  # nokia 1100 price is 2500
print(my_phone.__repr__())  # Phone('nokia','1100','2500')
print(len(my_phone))  # 10

print(my_phone+my_phone2)  # 5500
print(my_phone*my_phone2)  # 7500000

print(my_phone.phone_name())  # nokia 1100
print(smart_Phone.phone_name())  # OnePlus 5 60000
