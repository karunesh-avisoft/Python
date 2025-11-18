str = "Hello Avisoft!"

if "Avi" in str:
    print(True)
    
print('''
      Hi, my name is Karunesh.
      Currently staying in jammu and working
      as Software Engineer Trainee at
      Avisoft!''')


#match statement instead of switch statement
randomNum = 5
match randomNum:
    case 1:
        print('One')
    case 2:
        print('Two')
    case 3:
        print('Three')
    case _:
        print('Default')