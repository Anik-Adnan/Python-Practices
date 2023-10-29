from csv import DictReader, DictWriter
with open('214_read.csv', 'r') as rf:
    with open('214_another.csv', 'w', newline='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(
            wf, fieldnames=['First_Name', 'Last_Name', 'Age'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname, lname, age = row['first_name'], row['last_name'], row['age']
            csv_writer.writerow(
                {'First_Name': fname.upper(), 'Last_Name': lname.upper(), 'Age': age})
