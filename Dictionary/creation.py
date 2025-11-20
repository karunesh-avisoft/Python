dict={}     # empty dictionary
print(type(dict))


student={
    "name":"Karunesh",
    "company":"Microsoft",
    "location":"Jammu",
}
# print(student['pin'])     KeyError
# print(student.get('pin')) None

student['pin']=181500
print('Dictonary:',student)
print(student.popitem())
# print(student.popitem())
# print(student.popitem())
# print('Dictonary:',student)

