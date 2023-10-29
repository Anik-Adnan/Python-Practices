from csv import reader
with open('211_csvFile.csv', 'r') as f:
    csv_reader = reader(f)
    # iterator
    # print(csv_reader) # object
    next(csv_reader)  # ['name', 'email', 'phone']
    for row in csv_reader:
        print(row)
