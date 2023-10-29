# else and finally clause in exception handling
while True:
    try:
        age = int(input('enter  your age : '))
    except ValueError:
        print('invalid input')
    except:
        print('unexpected error .. ..')

    else:
        print('You can play this game.')
        print(f'You print {age} ')
        break
    finally:  # finally block all time executable
        print('finally block ... ')
