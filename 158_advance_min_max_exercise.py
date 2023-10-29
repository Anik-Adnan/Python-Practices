student = [
    {'name': 'anik', 'score': 90, 'age': 20},
    {'name': 'asif', 'score': 92, 'age': 23},
    {'name': 'farhad', 'score': 85, 'age': 21},
    {'name': 'biddut', 'score': 85, 'age': 25},
]
print(max(student, key=lambda item: item.get('score')))
print(max(student, key=lambda item: item.get('age')))
# print name
print(max(student, key=lambda item: item.get('score'))['name'])

student2 = {
    'anik': {'score': 90, 'age': 20},
    'asif': {'score': 95, 'age': 23},
    'farhad': {'score': 85, 'age': 21},
    'biddut': {'score': 85, 'age': 25},
}
print(max(student2, key=lambda item: student2[item]['score']))
print(max(student2, key=lambda item: student2[item]['age']))
