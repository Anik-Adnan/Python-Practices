class laptop:
    def __init__(self, brand_name, model_name, price):
        # instance variable
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + ' '+model_name + ' '+str(price)

    def apply_discount(self, number):
        # return self.price - self.price*(number/100)
        off_price = self.price * (number / 100)
        return self.price - off_price


l1 = laptop('hp', 'au114tx', 63000)
l2 = laptop('apple', 'macboook pro', 230000)
print(l1.price)
print(l1.laptop_name)
print(l2.apply_discount(5))
