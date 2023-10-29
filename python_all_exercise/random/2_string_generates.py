import random
import string

# defining function for random
# string id with parameter


def ran_gen(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


# function call for random string
# generation with size 8 and string
print(ran_gen(8, "AEIOSUMA23"))


# 2

# Generate a random string
# with 32 characters.
random = ''.join([random.choice(string.ascii_letters
                                + string.digits) for n in range(32)])

# print the random
# string of length 32
print(random)
