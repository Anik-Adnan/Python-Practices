def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as zero:
        # print('You cann\'t divide a number by zero')
        # ZeroDivisionError: division by zero er  "division by zero " printed
        print(zero)
    except TypeError as err:
        print(err)
    except:
        print('unexpected error')


print(divide(10, '0'))
# print(divide(10, 0))
# print(divide(10, 2))
