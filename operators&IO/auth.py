# Register
print('Register yourself>>')
regUser= input('Enter your username: ')
regPass = input('Enter your password: ')
print('Registration successful')
# Login
print('Now login yourself')
username = input('Enter your username: ')
password = input('Enter your password: ')


if username!=regUser and password!=regPass:
    print('Access denied, register yourself!')
elif username != regUser:
    print('Invalid username!')
elif password != regPass:
    print('Invalid password!')
else:
    print('Login successful.')
