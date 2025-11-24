# def test():
#     global x
#     x = 10
#     print(x)

# x=11
# print(x)
# test()

x = 10 # global
def local():
    global x
    x=15    # local
    print(x)
    
print(x)
local()

# def inside():
#     a=34
# print(a)

# non local
def container():
    x=20
    def outer():
        b=9
        print('outer called')
        def inner():
            nonlocal b
            b+=1
            print('from inner:',b)
        inner()
        inner()
    outer()
container()