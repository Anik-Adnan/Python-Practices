# function (returning function (closure) practice
def to_power(x):
    def calc_power(n):
        return n ** x
    return calc_power


cube = to_power(3)
print(cube(2))  # 2^3=8

square = to_power(2)
print(square(8))  # 64 {8^2==64}
