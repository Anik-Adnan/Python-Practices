def args_list(num,*agrs):
    if agrs:
        return [i**num for i in agrs ]
    else:
        return "hey!you didn't pass anr agrs"
list=[1,2,3,4,5]
print(args_list(3, *list))