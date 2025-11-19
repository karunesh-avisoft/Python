# create list using comprehension
squares=[val**2 for val in range(1,11)]
print('Squares in range 1 to 10:',squares)

# conditional comprehension
values=[10,-5,8,-3,12,-7,15]
evenOdd=['Even'  if val%2==0 else 'Odd' for val in values]
print('Even Odd list:',evenOdd)

# nested comprehension
X=[1,2,3]
Y=['A','B','C']

res=[(x,y) for x in X for y in Y]
print('Paired list:', res)

# list flattening
matrix=[[1,2,3],[4,5,6],[7,8,9]]
flattened=[val for row in matrix for val in row]
print('Flattened matrix:',flattened)