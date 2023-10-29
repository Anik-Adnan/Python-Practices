# dictionary comprehension with if else
# print {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}

odd_even = { i:('even' if i%2==0 else 'odd' )for i in range(1,11) }
print(odd_even)

for k,v in odd_even.items():
        print(f"{k} is : {v}")