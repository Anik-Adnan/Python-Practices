# Python supports a translate method on the str type which allows you to specify the translation table (used for
# replacements) as well as any characters which should be deleted in the process.

# str.translate(table[, deletechars])
# Parameter                   Description
# table It is a lookup table that defines the mapping from one character to another.
# deletechars A list of characters which are to be removed from the string.

# The maketrans method (str.maketrans in Python 3 and string.maketrans in Python 2) allows you to generate a
# translation table.


translation_table = str.maketrans("aeiou", "12345")
my_string = "This is a string!"
translated = my_string.translate(translation_table)
print(translated)
# 'Th3s 3s 1 str3ng!'

# # You can set the table argument to None if you only need to delete characters.
# translation_table = str.maketrans(None, 'aeiou')
# string = 'this syntax is very useful'
# translated = string.translate(translation_table)
# print(translated)
# # 'ths syntx s vry sfl'
