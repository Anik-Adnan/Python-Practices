#generate list with range function
#something more about pop fuction
#index method
#pass list to a function

number=list(range(1,11))
print(number)

# n=number.pop() #return removed value =10
# print(number)
# print(n)

#index method
#serching argument position
#number.index(5,serch starting index,ending index)
# print(number.index(5)) #5 's idex is 4 means argument position
# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,2,16,17]
# print(a.index(2,11)) #a[14]=2
##print(a.index(2,11,15)

def negative_list(n):
    negative=[]
    for i in n:
        negative.append(-i)
    return negative
print(negative_list(number))