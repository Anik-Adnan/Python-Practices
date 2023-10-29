#why we use dictionaries?
# because of limtations of lists, lists are not enough  to represent
# real data

#exmple
user = ['anik','22',['coco', 'kimi no na wa'], ['awakening', 'fairy tale']]
# this list contains user name, age, fav movies, fav tunes
# you can do this but this is not a good way to do this

# what are dictionaries/
# unordered collections of data in key : value pair.

#how to create dictionaries
user ={'name' : 'Anik Adnan',
        'age': 24}
print(user)
print(type(user))
#another way
a= dict( name= "adna", age = 25)
print(a)

#no indexing in a dictionaries
#for acessing 
print(user['name'])
print(a['age'])

user_info = {'name':'anik',
            'age':22,
            'fav_movies' :['coco', 'kimi no na wa'], 
            'fav_tunes' : ['awakening', 'fairy tale']
}
print(user_info['fav_movies'])

#how to add data to empty dictionary
user_info2={}
user_info2['name'] = 'mohid'
print(user_info2['name'])
print(user_info2)
