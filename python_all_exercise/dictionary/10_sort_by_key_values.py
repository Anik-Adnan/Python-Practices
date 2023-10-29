# Declare hash function
key_value = {}

# Initializing value
key_value["a"] = 1
key_value["b"] = 2
key_value['e'] = 5
key_value['c'] = 3
key_value['x'] = 15
key_value['d'] = 4


def dictionairy():
    print("Task 1:-")
    print("Keys are")

    # iterkeys() returns an iterator over the
    # dictionary’s keys.
    for i in sorted(key_value.keys()):
        print(i, end=" ")


dictionairy()


def dictionairy2():

    print("\nTask 3:-\nKeys and Values sorted",
          "in alphabetical order by the value")

    # Note that it will sort in lexicographical order
    # For mathematical way, change it to float
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))


dictionairy2()
