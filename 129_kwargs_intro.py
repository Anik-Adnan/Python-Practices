# kargs ( keyword arguments)
# ** kwargs( double star operator)

# kwargs as a parameter
def func(**kwargs):
    print(kwargs)
    print(type(kwargs)) # <class 'dict'>
    for k,v in kwargs.items():
        print(f"{k} is : {v}")
    print(f"Full_name is : {kwargs['first_name'] +' '+ kwargs['last_name']}")
    
# func(first_name = 'Anik', last_name = 'Adnan')
# dictionary unpacking
d = {'first_name': 'Anik', 'last_name': 'Adnan'}
func(**d)