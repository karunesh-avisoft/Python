test_case={
    "id": 101,
    "name": "Login test",
    "status": "Not executed",
    "steps": ["Open brower", "Enter username", "Enter password", "Click login"]
}
print('Test case:', test_case)

print("Steps:")
for idx,step in enumerate(test_case["steps"], 1):
    print(f'{idx}: {step}')

test_case["status"]="Passed"
test_case["priority"]="High"
print('Test case:', test_case)

# Methods
print("Keys:",test_case.keys())
print("Values:",test_case.values())
print("Items:",test_case.items())

test_case.update(name="Login")
test_case.update(new=list((1,2,3)))

print(test_case.pop("new"))
print(test_case)


# nested dictionary
test_suite={
    "smoke": {"TC01":"Passed", "TC02":"Failed"},
    "regression": {"TC10":"Passed", "TC11":"Skipped"}
}

regression=test_suite["regression"].items()
for testcases in regression:
    print(testcases)
    
# test_suite["smoke"]["TC02"]='Pass'
# test_suite["smoke"].update(TC02='Passed')
test_suite["smoke"].update({'TC02':'Skipped'})

print(test_suite)