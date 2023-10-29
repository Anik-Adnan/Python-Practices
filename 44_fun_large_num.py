#print large number bwt 2 numbers in afuncton
a=int(input("enter first number  : "))
b=int(input("enter second number : "))
def large_num(a,b):
    if a>b:
        return a
    return b
print(f"large number is  : {large_num(a,b)}")