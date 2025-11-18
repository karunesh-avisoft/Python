name = input('Enter your name: ')
favTech = input('Enter your favourite technology: ')

print("Hello,", name,"your favourite technology is", favTech,".")

# formatted string
print('using f-string')
print(f"Hello {name} your favourite technology is {favTech}.")

print('using format method')
print("Hello {} your favourite technology is {}." .format(name,favTech))
# print("Hello %s your favourite technology is %s." %(name,favTech))

print(name.upper())

# modifiers
print(f'The price for its course is {45000:.2f}')
print(f'The price for its course is {45000:,}')
