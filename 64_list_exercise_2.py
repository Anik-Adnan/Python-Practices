
    # reverse=[]
    # for i in n:
    #     reverse.pop()
    #     reverse.append(i)

# def reverse_list(n):
#     n.reverse()
#     return n
# number=[1,2,3,4]
# print(reverse_list(number))

# def reverse_list(n):
#     return n[::-1]
# number=[1,2,3,4]
# print(reverse_list(number))

def reverse_list(n):
    rev_list=[]
    for i in range(1,len(n)+1):
        pop_item=n.pop()
        rev_list.append(pop_item)
    return rev_list
number=[1,2,3,4]
print(reverse_list(number))