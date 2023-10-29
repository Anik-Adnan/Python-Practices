def CountFrequency(my_list):

    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print("% d : % d" % (key, value))


my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
CountFrequency(my_list)

print()

# 22222222


def CountFrequency2(my_list):

    # Creating an empty dictionary
    freq = {}
    for items in my_list:
        freq[items] = my_list.count(items)

    for key, value in freq.items():
        print("% d : % d" % (key, value))


CountFrequency(my_list)


# 333333333
def CountFrequency3(my_list):

    # Creating an empty dictionary
    count = {}
    for i in [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]:
        count[i] = count.get(i, 0) + 1
    return count


my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
print(CountFrequency3(my_list))
