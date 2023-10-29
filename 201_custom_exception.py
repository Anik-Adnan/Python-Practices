# python custom exceptions
# Q- why custom exception ?
# A- to increase the readability of code

class NameTooShortError(ValueError):
    pass


def validate(name):
    if len(name) < 8:
        # raise ValueError('name is too short')
        raise NameTooShortError('name is too short')


username = input('Enter  your name : ')
validate(username)
print(f'hello {username}')
