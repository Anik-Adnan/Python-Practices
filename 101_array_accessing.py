# Individual elements can be accessed through indexes. Python arrays are zero-indexed.
import array
a = array.array('i' , [1, 2 , 4 , 6 ,8])
print(a[0]) # print a[0]= 1
for i in a:
    print(i, end=' ')