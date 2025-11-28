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
print()
    # eg 
def describe_person(**info):
    print(info)

describe_person(name="Alice", age=20, country="USA")

def describe_args(*args):
    print(args)

describe_args(1,2,3,4,5)

# method overloading
def area(shape, *dimensions):
    if shape == "circle" and len(dimensions) == 1:
        r = dimensions[0]
        return 3.14 * r * r

    elif shape == "rectangle" and len(dimensions) == 2:
        w, h = dimensions
        return w * h

    elif shape == "square" and len(dimensions) == 1:
        s = dimensions[0]
        return s * s

    else:
        return "Invalid parameters"

print(area("circle", 5))      # 78.5
print(area("rectangle", 4, 6))# 24
print(area("square", 3))      # 9



