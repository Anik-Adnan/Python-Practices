# dictionary comprehension
# key value pair
square = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
square = { f"Square if {num} is ":num**2  for num in range(1, 11)}
for k,v in square.items():
    print(f"{k} : {v}")

print('word count')

string = "Anik Adnan Biswas"
word_count = { char: string.count(char) for char in string}
print(word_count)
