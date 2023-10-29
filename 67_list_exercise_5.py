#common element between two list 
def common_list(n1,n2):
    output=[]
    for i in n1:
        if i in n2:
            output.append(i)
    return output
n1=[1,2,3,4]
n2=[2,5,3] 
print(common_list(n1,n2))