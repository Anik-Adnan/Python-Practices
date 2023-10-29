print(3 % 4) # 3
import operator
print(operator.mod(6,4)) # 2
print(operator.mod(-9, 7)) # 5
print(operator.mod(9, -7))  # -5
print(operator.mod(-9, -7)) # -2

# divmod
quotient, reminder = divmod(9 ,4)
print(quotient) # quotient = 2 
print(reminder)  # remainder = 1
