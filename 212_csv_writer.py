from csv import writer
with open('212_csv_file2.csv', 'w', newline='') as f:
    csv_writer = writer(f)
    # methods --> writerows, writerow

    # csv_writer.writerow(['name', 'countries'])
    # csv_writer.writerow(['Anik', 'bangladesh'])
    # csv_writer.writerow(['fayek', 'india'])

# same output but list inside list (multipul rows)
# sowing error if one list pass
    csv_writer.writerows(
        [['name', 'countries'], ['Anik', 'bangladesh'], ['fayek', 'india']])
