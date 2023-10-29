import math
C, H = 50, 30


def calc(D):
    return math.sqrt((2*C*D)/H)


# splits in comma position and set up in list
D = [int(i) for i in input().split(',')]
D = [int(i) for i in D]   # converts string to integer
# returns floating value by calc method for every item in D
D = [calc(i) for i in D]
D = [round(i) for i in D]  # All the floating values are rounded
# All the integers are converted to string to be able to apply join operation
D = [str(i) for i in D]

print(",".join(D))
