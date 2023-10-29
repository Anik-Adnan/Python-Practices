class laptop:
    discount_percentage = 10

    def __init__(self, brand_name, model_name, price):
        # instance variable
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + ' '+model_name + ' '+str(price)

    def apply_discount(self):
        # return self.price - self.price*(number/100)
        off_price = (self.discount_percentage/100)*self.price
        return self.price - off_price


l1 = laptop('hp', 'au114tx', 63000)
l2 = laptop('apple', 'macboook pro', 230000)
l2.discount_percentage = 50
print(l2.__dict__)
print(l2.apply_discount())
