#count method
#sort method
#sorted function
#reverse method
#clear method
#copy method

print("count method")
name=['apple','guava','apple','grap','mango','ball','coconut']
print(name.count('apple')) #count apple

print("sort method")
#sorting elemens with alphabetical
name.sort()
print(name)
#sorting number
number=[10,3,30,7,15,500,17,35]
number.sort()
print(number)
#if you don't want to sort your list 
#but you want to print sorted order list
number=[10,3,30,7,15,500,17,35]
print(sorted(number))
print(f"real list={number}")


#clear method clearing your list
print("clear method")
number=[10,3,30,7,15,500,17,35]
number.clear()
print(number)

#copy method copying your list
print("copy method")
number=[10,3,30,7,15,500,17,35]
number_copy=number.copy()
print(number_copy)
print(number)

#reverse method clearing your list
print("reverse method")
number=[10,3,30,7,15,500,17,35]
number.reverse()
print(number)