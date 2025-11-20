api_params=('GET','/login',200)
# unpack
method,endpoint,status=api_params

print('method:',method)
print('endpoint:',endpoint)
print('status:',status)

test_cases=('signup','login','loading','redirection','exceptions')

print('Printing test cases...')
# for test in test_cases:
#     print(test)

# i = 0
# while i<len(test_cases):
#     print(f'{i}: {test_cases[i]}')
#     i += 1

# enumerate
for i,test in enumerate(test_cases):
    print(f'{i}: {test}')
    
    
# eval will automatically type cast the input value to is original data type such as: 1 to 'int'
tup=eval(input('Enter something to tuple:'))
print(tup)
print(type(tup))