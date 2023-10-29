#print large number bwt 3 numbers in afuncton
#programing rules
#kiss --> keep it simple stupid

a=int(input("enter first number  : "))
b=int(input("enter second number : "))
c=int(input("enter third  number : "))
# def large_num(a,b):
#     if a>b:
#         return a
#     return b
# l=large_num(a,b)
# def bigest(l,c):
#     if l<c:
#         return c
#     return l
# print(f" large  number  is  : {bigest(l,c)}")

def large_num(a,b):
    if a>b:
        return a
    return b
def new_large(a,b,c):
        return large_num(large_num(a,b),c)
print(f"large  number  is  : {new_large(a,b,c)}")
