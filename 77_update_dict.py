user_info = {'name':'anik',
            'age':22,
            'fav_movies' :['coco', 'kimi no na wa'], 
            'fav_tunes' : ['awakening', 'fairy tale']
}

more_info= {'name': 'anik adnan' ,
'fav_song' : [ 'song1','song2' ] }
#name updated not add a new key and item
user_info.update(more_info)
print(user_info)

# user_info.update({}) #empty dict.


