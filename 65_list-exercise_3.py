#reverse  every words in a list
def reverse_list(n):
    rev_list=[]
    for i in n:
        rev_list.append(i[::-1])
    return rev_list
number=['anik',"adnan",'Biswas']
print(reverse_list(number))