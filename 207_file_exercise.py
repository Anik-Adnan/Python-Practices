# anik,100
# adnan,200
# rahid,500

# output
# anik's salary is 100
# adnan's salary is 200
# rahid's salary is 500

with open('salary_207.text', 'r') as rf:
    with open('output_207.text', 'a') as wf:
        for line in rf.readlines():
            name, salary = line.split(',')
            wf.write(f"{name}'s salary id {salary}")
