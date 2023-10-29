a = ['abc', 'xyz', 'pqr']
# print ['cba', 'zyx', 'rqp']
a = [ i[::-1] for i in a]
print(a)

def reverse_str(list):
    return [i[::-1] for i in list]
print(reverse_str(['anik','adnan', 'biswas']))


def reverse_string(list):
    new_list= []
    for name in list:
        new_list.append(name[::-1])
    return new_list
print(reverse_string(['momotuz', 'pervin','biswas']))