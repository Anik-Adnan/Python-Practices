# multipul inheritence

class A:
    def class_a_method(self):
        return "I'm just a class A method"

    def hello(self):
        return 'hello from class a'


class B():
    def class_b_method(self):
        return "I'm jus a class B method"

    def hello(self):
        return "hello from B"


class C(A, B):
    pass


instance_c = C()
print(instance_c.class_a_method())  # I'm just a class A method
print(instance_c.hello())  # hello from class a
print(instance_c.class_b_method())  # I'm jus a class B method
print(instance_c.hello())  # hello from class a

# # print(help(instance_c))
# # Method resolution order:
# #  |      C
# #  |      A
# #  |      B
# #  |      builtins.object
# print(C.mro())
# # [<class '__main__.C' > , <class '__main__.A' > , <class '__main__.B' > , <class 'object' > ]

# print(C.__mro__)
# # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
