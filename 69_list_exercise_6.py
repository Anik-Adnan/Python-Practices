#how many list inside a list
def sublist_counter(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count
mixed_list=[1,2,3,['anik'],10 ,15,[20 ,54],['adnan']]
print(sublist_counter(mixed_list))