def charCount(word):
    d = dict()
    for i in word:
        d[i] = d.get(i, 0) + 1
    return d


def possible_words(l, charSet):

    for word in l:
        flag = 1
        chars = charCount(word)
        for k in chars:
            if k not in charSet:
                flag = 0
            else:
                if charSet.count(k) != chars[k]:
                    flag = 0
        if flag == 1:
            print(word)


l = ['goo', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
possible_words(l, charSet)
