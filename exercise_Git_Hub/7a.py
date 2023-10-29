input_str = input()
dimensions = [int(x) for x in input_str.split(',')]
row_num = dimensions[0]
col_num = dimensions[1]
multilist = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multilist[row][col] = row * col

print(multilist)
