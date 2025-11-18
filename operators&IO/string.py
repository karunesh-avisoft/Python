name = input('Enter your name: ')
favTech = input('Enter your favourite technology: ')

print("Hello,", name,"your favourite technology is", favTech,".")

# using formatted string
print('f-string')
print(f"Hello {name} your favourite technology is {favTech}.")
print("Hello {} your favourite technology is {}." .format(name,favTech))
print("Hello %s your favourite technology is %s." %(name,favTech))

