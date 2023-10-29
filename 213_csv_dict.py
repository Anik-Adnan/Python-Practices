from csv import DictWriter
with open('213_dict.csv', 'w', newline='') as f:
    csv_writer = DictWriter(f, fieldnames=['first_name', 'last_name', 'age'])
    csv_writer.writeheader()
    #  writerow input as a dictionary
    # csv_writer.writerow(
    #     {'first_name': 'Anik', 'last_name': 'Adnan', 'age': 21})
    # csv_writer.writerow(
    #     {'first_name': 'Asif', 'last_name': 'Adnan', 'age': 22})
    # csv_writer.writerow(
    #     {'first_name': 'fadhad', 'last_name': 'Hossain', 'age': 21})

    # writerows --> [dict,dict,dict]
    csv_writer.writerows([
        {'first_name': 'Anik', 'last_name': 'Adnan', 'age': 21},
        {'first_name': 'Asif', 'last_name': 'Adnan', 'age': 22},
        {'first_name': 'fadhad', 'last_name': 'Hossain', 'age': 21}
    ])
