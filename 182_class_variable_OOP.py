# class veriable
# circle
# area
# circum

class Circle:
    # class veriable
    # call Class_name.variable_name
    # Circle,pi
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def cal_circumference(self):
        return 2 * Circle.pi * self.radius


c = Circle(4)
print(c.cal_circumference())
