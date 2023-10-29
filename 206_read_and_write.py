with open('file4.text', 'r') as rf:
    with open('file5.text', 'w') as wf:
        wf.write(rf.read())
