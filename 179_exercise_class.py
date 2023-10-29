class laptop:
    def __init__(self, brand_name, model_name, price):
        # instance variable
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + ' '+model_name + ' '+str(price)


l1 = laptop('apple', 'probook', 70000)
l2 = laptop('hp', 'au114tx', 63000)

print(l2.price)
print(l2.laptop_name)
