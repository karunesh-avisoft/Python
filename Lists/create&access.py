# fruits = list(("apple","banana","cherry","date","elderberry"))
fruits = ["apple","banana","cherry","date","elderberry"]
print(fruits)
print('3rd item:',fruits[2])
print('last item:',fruits[-1])
print('second last item:',fruits[-2])

# modify
colors = ["red","blue","green","yellow"]
colors[1]= "purple"
colors[-1]="orange"

print('colors:',colors)

# using enumerate
for idx,val in enumerate(colors,1):  # we can give starting value as second arg
    print(f'{idx}. {val}')
