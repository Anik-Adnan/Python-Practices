# raise error
class Mobile:
    def __init__(self, name):
        self.name = name


class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mobile should be object of mobile class')

        return self.mobiles.append(new_mobile)


oneplus = Mobile('one plus 7')
samsung = 'samsumg galaxy s10'
mobostore = MobileStore()

# without istance
# mobostore.add_mobile(samsung)
# print(mobostore.mobiles) # ['samsumg galaxy s10']

# after using instance
# mobostore.add_mobile(samsung)  # error isinstance else called
# print(mobostore.mobiles)

mobostore.add_mobile(oneplus)
mobo_phones = mobostore.mobiles
print(mobo_phones[0].name)
