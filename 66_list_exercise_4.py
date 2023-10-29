#odd or evev number inside list between two list
def even_odd(n):
    even=[]
    odd=[]
    for i in n:
        if i %2 ==0:
            even.append(i)
        else:
            odd.append(i)
    output=[odd,even]
    return output
n=[1,2,3,4,5,6,7,8,9]
print(even_odd(n))