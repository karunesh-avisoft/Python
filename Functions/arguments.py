def greet(name='Guest'):
    print('Hello ',name)
    
greet()
greet('Harshit')

def power(x,n=2):
    print(x**n)

power(5)
power(2,5)

# unpacking keyword arguments
def details(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')
        
details(name='Ana',age=6, standard='3rd')

# calling via keyword arguments
def order(item, quantity):
    print(f'Order: {item}={quantity} unit')

order(item='COCO',quantity=150)
    
