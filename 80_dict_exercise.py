# define a function that takes a number(n)
# return a dictionary containing cube of this numbers 1 to n

def cube_of_n(n):
    cube={}
    for i in range(1,n+1):
        cube[i]=i**3
    return cube

print(cube_of_n(3))