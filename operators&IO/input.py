name = input('Enter your name:')
print('Welcome!', name)

side = float(input('Enter the side of the sqaure:'))
area = side**2
print('Area of square: ',area)




a = list(input("List1: "))
b = list(input("List2: "))
for i in b:
    a.append(i)

print("Final List:", a)