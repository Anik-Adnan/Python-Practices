# store data from user 

user = {}
name = input('what is your name  ? ')
age =int(input('what is your age ? '))
fav_movies= input('enter your favourite movies separated by comma : ').split(',')
fav_songs= input('enter your favourite songs separated by comma : ').split(',')

user['name']= name
user['age']= age
user['fav_movies']= fav_movies
user['fav_songs']=fav_songs
print(user)

for key,value in user.items():
    print(f'{key} is  {value}')

