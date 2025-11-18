a,b = input('Enter any two number: ').split(',')
a=int(a)
b=int(b)

print('------arithmetic operators')
print('Sum:', a+b)
print('Difference:', a-b)
print('Product:', a*b)
print('Division:', a/b)
print('Floor Division:',a//b)
print('Remainder:', a%b)

print('-----contitionl operators')
print(a==b)
print(a!=b)
print(a>=b)
print(a<b)
print(a<=b)
print(a>b)
print(a<<b)

print('-----logical operators')
print('and ', a>b and a<b)
print('or ', a>b or a<b)
print('not ', not True)


print('-----identity operators')

x = ['abs']
y = ['abs']
print(x is y) #false as they are diff objects
print(x == y)







