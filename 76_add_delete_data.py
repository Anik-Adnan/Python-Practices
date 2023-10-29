# add  and delete data
user_info = {'name':'anik',
            'age':22,
            'fav_movies' :['coco', 'kimi no na wa'], 
            'fav_tunes' : ['awakening', 'fairy tale']
}
# add data
print("add data")
user_info['fav_song']=['song1','song2']
print(user_info)
#pop method(at least one argument pass in the method)
poped_item=user_info.pop('fav_tunes')
print(poped_item)
print(user_info)

#popitem metod
#random delete item
pop_item=user_info.popitem()
print(f'popitem is {pop_item}')
print(type(pop_item))