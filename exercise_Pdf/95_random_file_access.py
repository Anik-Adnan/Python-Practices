# Using the mmap module allows the user to randomly access locations in a file by mapping the file into memory. This
# is an alternative to using normal file operations.
import mmap
with open('myfile2.txt', 'r') as fd:
    # 0: map the whole file
    mm = mmap.mmap(fd.fileno(), 0)
    # print characters at indices 5 through 10
    print(mm[5:10])
    # print the line starting from mm's current position
    print(mm.readline())
    # write a character to the 5th index
    mm[5] = 'a'
    # return mm's position to the beginning of the file
    mm.seek(0)
    # close the mmap object
    mm.close()
