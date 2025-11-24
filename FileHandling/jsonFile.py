import json

data={'name': 'QATester','score':85,
      "test_cases":[
        {"id":1,"status":"pass"},
        {"id":2,"status":"fails"}
      ]}

with open('data.json','w') as f:
    json.dump(data,f,indent=4)

with open('data.json','r') as f:
    info=json.load(f)
    print(info)

# newline delimited JSON(NDJSON) for writing multiple objects in a json file
# import json

# data = {'name': 'QATester','score':85}
# test_data = {
#     "test_cases":[
#         {"id":1,"status":"pass"},
#         {"id":2,"status":"fails"}
#     ]
# }

# with open("data.json", "w") as f:
#     f.write(json.dumps(data) + "\n")
#     f.write(json.dumps(test_data) + "\n")

# # print line by line for to avoid extra data error
# with open("data.json", "r") as f:
#     for line in f:
#         obj = json.loads(line)
#         print(obj)


tests={
    'suite':[
        {'id':1,'result':'pass'},
        {'id':2,'result':'fail'},
        {'id':3,'result':'pass'},
        {'id':4,'result':'fail'},
    ]
}

with open('tests.json','w') as f:
    json.dump(tests,f)
    
with open('tests.json', 'r') as f:
    res=[]
    for test in tests['suite']:
        if test['result']=='fail':
            res.append(test['id'])
    print(res)
    
