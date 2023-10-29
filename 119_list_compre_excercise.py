list = [ 'anik',['adnan',20,1998], 2000, 1, 5.5, 10]
def num_to_string(list):
    return [ str(i) for i in list if (type(i)== int or type(i)== float) ]
# print ['2000', '1', '5.5', '10']
print(num_to_string(list))