# lambda function
a=5
b=10
c=lambda a,b:a+b
print(c(a,b))

sqr=lambda b:b**2
print(sqr(b))

# celsius to fahrenheit map()
celsius=[10,25,35,48,50]
fahrenheit=map(lambda x:x*9//5+32,celsius)

print('Fahrenheit:',list(fahrenheit))

# odd number with filter()
nums=[2,3,5.35,56,8,97,66]
even=filter(lambda x:x%2==0,nums)
print(even)
print(list(even))

# last character of string
word="character"
ch=lambda x:x[-1]
print('Last character:',ch(word))