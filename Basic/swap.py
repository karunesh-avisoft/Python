a = 5
b = 7

print("before ", a, b)
a,b=b,a

# using third variable
def swap1(a,b):
    temp = a
    a = b
    b = temp
    return a, b
    
# without third variable
def swap2(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a, b
    
# a,b = swap2(a,b)

print('after ', a, b)
    