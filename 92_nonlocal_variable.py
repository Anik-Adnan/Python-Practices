def counter():
    num = 0
    def incrementer():
        nonlocal num # if u donot use nonlocal UnboundLocalError
        num += 15
        return num
    return incrementer()

print(counter())