# creating & accessing
fruits=("apple","banana","papaya",'kiwi','pomogranate')
print('Fruits:',fruits)
print(fruits[1])
print(fruits[3])


# unpacking tuples
t=(10,20,30)
x,y,z=t
print('x:',x)
print('y:',y)
print('z:',z)
print('Length:',len(t))

# methods
states=('Delhi','Haryana','Punjab','Jammu&Kashmir','Delhi','Uttar Pradesh')
print('Count of states:',states.count('Delhi'))        # count
print('Index of Punjab:',states.index('Punjab'))    # index
# print(states.index('UP')) value error: 'UP' not in tuple
print('Sliced tuple:',states[2::2])
print('Reversed tuple:',states[::-1])

