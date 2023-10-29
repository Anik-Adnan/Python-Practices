# w, a ,r+

# with open('file2.text', 'a') as f:
#     data = f.write('\nThis is append mode')

with open('file3.text', 'r+') as f:
    # data = f.write('This is r+ mode \n') # This is r+ mode
    # data = f.write('that \n')  # this overwriten
    f.seek(len(f.read()))
    f.write('please do it\n')
