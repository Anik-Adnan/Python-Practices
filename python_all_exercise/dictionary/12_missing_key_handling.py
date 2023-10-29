# initializing Dictionary
d = {'a': 1, 'b': 2}

# trying to output value of absent key
print("The value associated with 'c' is : ")
# print(d['c']) #error

country_code = {'India': '0091',
                'Australia': '0025',
                'Nepal': '00977'}

# search dictionary for country code of India
print(country_code.get('India', 'Not Found'))

# search dictionary for country code of Japan
print(country_code.get('Japan', 'Not Found'))
