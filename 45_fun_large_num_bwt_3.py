#print large number bwt 3 numbers in afuncton
a=int(input("enter first number  : "))
b=int(input("enter second number : "))
c=int(input("enter third  number : "))
def large_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>c :
        return b
    return c
print(f" large  number  is  : {large_num(a,b,c)}")