# Functions

def provide_sum(a,b):
    return a+b

sum=provide_sum(55,20)
print('Sum:',sum)

# print even numbers
nums=[1,2,3,4,5,67,8,9,0]
def even_num(a:'list'):
    for num in a:
        if num%2==0:
            print(num)
    
even_num(nums)

# check pallindrome
# input='racecar'
inp='madaam'

def isPallindrome(inp:'str'):
    if inp==inp[::-1]:
        return 'Pallindrome'
    else:
        return 'Not Pallindrome'
    
print(isPallindrome(inp))

def display(name:'str'='karu',age:'int'=22):
    print(f'I am {name} and I am {age} years old.')

# display()
# display('karunesh')
# display(45)
display(name='ritik')   # positioned arguments

#  count vowels
def count_vowels():
    inp=input('Enter a string:')
    count=0
    for char in inp:
        if char in list(('a','e','i','o','u','A','E','I','O','U')):
            count+=1
            
    print('Count of vowels:',count)
    
count_vowels()
        
