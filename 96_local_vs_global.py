foo = 1 # global
def func():
    bar = 2 # local
    #global foo
    foo= 15
    print(foo) # prints variable foo from global scope
    print(globals()['foo'])
    print(locals().keys()) # dict_keys(['bar', 'foo'])
    print('foo' in locals()) # True 
    print('bar' in globals()) # False
    print(bar) # prints variable bar from local scope
func()
print(foo)

# One can inspect which variables are in which scope. Built-in functions locals() and globals() return the whole
# scopes as dictionaries.
# foo = 1
# def func():
#     bar = 2
#     print(globals().keys()) # prints all variable names in global scope
#     print(locals().keys()) # prints all variable names in local scope
# func()

# foo = 1
# def func():
#     foo = 2 # creates a new variable foo in local scope, global foo is not affected
#     print(foo) # prints 2
#     # global variable foo still exists, unchanged:
#     print(globals()['foo']) # prints 1
#     print(locals()['foo']) # prints 2
# func()

# foo = 4
# def func():
#     # This function has a local variable foo, because it is defined down below.
#     # So, foo is local from this point. Global foo is hidden.
#     #print(foo) # raises UnboundLocalError, because local foo is not yet initialized

#     # In this function, foo is a global variable from the beginning
#     foo = 7 # global foo is modified
#     print(foo) # 7
#     print(globals()['foo']) # 7
#     #global foo # this could be anywhere within the function
#     print(foo) # 7
# func()