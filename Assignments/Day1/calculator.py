print('Enter two numbers.')
a = int(input('a:'))
b = int(input('b:'))

print('Operations>>')
print('1 - Add')
print('2 - Subtract')
print('3 - Multiply')
print('4 - Divide')

ch = int(input('Enter your choice:'))

if ch == 1:
    print('Addition is-', a+b)
elif ch == 2:
    print('Substraction is-', a-b)
elif ch==3:
    print('Multiplication is-',a*b)
elif ch==4:
    if b==0:
        print('ERROR: Division by zero')
    else:
        print('Division is-',a/b)
else:
    print('Invalid choice...!')
    

