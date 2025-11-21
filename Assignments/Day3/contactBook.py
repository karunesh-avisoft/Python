print("\t\t\tCONTACT BOOK")
print('----------------------------------------------------------------')

contactBook={
    'Karunesh':{
        'phone': 9679475673,
        'email': 'karunesh@avisoft.io',
        'city': 'Jammu'
    },
    'Divyansh':{
        'phone': 9679475673,
        'email': 'divyansh@avisoft.io',
        'city': 'Gurugram'
    },
    'Ayush':{
        'phone': 9679475673,
        'email': 'ayush@avisoft.io',
        'city': 'Himachal'
    },
    'Ritik':{
        'phone': 9679475673,
        'email': 'ritik@avisoft.io',
        'city': 'Jammu'
    },
    'Harshit':{
        'phone': 9679475673,
        'email': 'harshit@avisoft.io',
        'city': 'Jammu'
    },
}

print('\t\tAvailable contacts:')
# using keys
# for name in contactBook.keys():
#     print(f'{name}: {contactBook[name]}')
# print()   
# using values
# for details in contactBook.values():
#     print(details)

# using items
for name,contact in contactBook.items():
    print(f'{name}: {contact}')

print()
proceed='y'     # user consent
while proceed.lower()=='y':
    print('  ***ACTIONS MENU***')
    print('''    1. All contacts
    2. Search
    3. Add new contact
    4. Update contact
    5. Delete contact
    6. Delete All''')
    print()
    choice=eval(input('Enter your action:'))
    
    if choice not in range(1,7):
        print('ERROR:Invalid Action!!')
        print()
    else:
        isEmpty=True if not len(contactBook) else False  # len return 0 if empty
        match choice:
            case 1:     # display all contacts
                if not isEmpty:
                    print('*****ALL CONTACTS*****')
                    print('---------------------------')
                    print()
                    for name,details in contactBook.items():
                        print(f"Name: {name}")
                        print(f"  Contact: {details['phone']}")
                        print(f"  Email: {details['email']}")
                        print(f"  City: {details['city']}")
                        print()
                else:
                    print('Sorry no contact avialable!!')
                    print()
            case 2:     # search logic
                if isEmpty:
                    print('Sorry no contact avialable!!')
                    print()
                else:
                    print('How do you want to search?')
                    print(f'  1. Name')
                    print(f'  2. City')
                    print(f'  3. Exit')
                    print()
                    choiceSearch=eval(input('Enter search choice:'))
                    while choiceSearch not in range(1,3):
                        print('Invalid search choice!!')
                        print()
                        choiceSearch=eval(input('Enter search choice:'))
                    if choiceSearch==1:
                        name=input('Enter name to search:')
                        print()
                        found=False
                        for contactName in contactBook.keys():
                            if name.lower() in contactName.lower():
                                found = True
                        if found:
                            print(f"Name: {details['name']}")
                            print(f"  Contact: {details['phone']}")
                            print(f"  Email: {details['email']}")
                            print(f"  City: {details['city']}")
                            print()
                        else:
                            print(f'Contact not found with name {name}!!')
                            print()
                    elif choiceSearch==2:
                        city=input('Enter the city to search:')
                        print()
                        found=[]
                        for name in contactBook.keys():
                            if city.lower() in contactBook[name]["city"].lower():
                                found.append(name)
                        if len(found)!=0:
                            for name in found:
                                print(f"Name: {name}")
                                print(f"  Contact: {contactBook[name]['phone']}")
                                print(f"  Email: {contactBook[name]['email']}")
                                print(f"  City: {contactBook[name]['city']}")
                                print()
                        else:
                            print(f'There is no contact from city {city}!!')
                            print()
                    elif choiceSearch==3:
                        print('Exit from search successfully!')
                        print()
            case 3:     # add logic
                name=input('Enter contact name:')
                print()
                if name not in contactBook.keys():
                    phone=input('Enter contact number:')
                    print()
                    while not (phone.isdigit() and len(phone)==10):
                        print('ERROR: Enter a valid number!!')
                        phone=input('Enter contact number:')
                        print()
                    phone=int(phone)
                    email=''
                    while '@' not in email:
                        email=input('Enter e-mail of the person:')
                        print()
                        if '@' not in email:
                            print('ERROR: Enter a valid e-mail!!')
                    city=input('Enter city of the person:')
                    print()
                    contactBook[name.capitalize()]={'phone':phone, 'email':email, 'city':city}
                    print('Contact saved successfuly!')
                    print()
                else:
                    print('ERROR: Duplicate entry!!')
                    print()
            case 4:     # update logic
                name=input('Enter contact name you want to update:')
                print()
                if name not in contactBook.keys():
                    print('No such contact exists!!')
                    print()
                else:
                    print('What do you want to update?')
                    print(f'  a. Phone')
                    print(f'  b. E-mail')
                    print(f'  c. City')
                    print(f'  d. Phone,e-mail & city')
                    print(f'  e. Exit')
                    print()
                    updateChoice=input('Enter your choice to update:').lower()
                    while updateChoice not in list(('a','b','c','d','e')):
                        print('ERROR:Enter a valid option to update!!')   
                        print()
                        updateChoice=input('Enter your choice to update:').lower()
                    match updateChoice:
                        case 'a':       # update phone
                            phone=input('Enter contact number:')
                            while not (phone.isdigit() and len(phone)==10):
                                print('ERROR: Enter a valid number!!')
                                print()
                                phone=input('Enter contact number:')
                            phone=int(phone)
                            contactBook[name.capitalize()]={'phone':phone}
                            print('Contact number updated successfully!')
                            print()
                        case 'b':       # update email
                            email=''
                            while '@' not in email:
                                print('ERROR: Enter a valid e-mail!!')
                                print()
                                email=input('Enter e-mail of the person:')
                            contactBook[name.capitalize()]={'email':email}
                            print("Contact's e-mail updated successfully!")
                            print()
                        case 'c':       # update city
                            city=input('Enter city of the person:')
                            contactBook[name.capitalize()]={'city':city}
                            print("Contact's city updated successfully!")
                            print()
                        case 'd':       # update all
                            phone=input('Enter contact number:')
                            while not (phone.isdigit() and len(phone)==10):
                                print('ERROR: Enter a valid number!!')
                                print()
                                phone=input('Enter contact number:')
                            phone=int(phone)
                            email=''
                            while '@' not in email:
                                print('ERROR: Enter a valid e-mail!!')
                                print()
                                email=input('Enter e-mail of the person:')
                            city=input('Enter city of the person:')
                            print()
                            contactBook[name.capitalize()]={'phone':phone, 'email':email, 'city':city}
                            print('Contact updated successfully!')
                            print()
                        case e:
                            print('Exit from update successfully!')
                            print() 
            case 5:     # delete logic
                name=input('Enter contact name you want to delete:')
                if name not in contactBook.keys():
                    print('Contact does not exists!!')
                    print()
                else:
                    contactBook.pop(name)
                    print(f'{name} deleted succefully!')
                    print()
            case 6:     # delete all
                if isEmpty:
                    print('Contact-book is already empty!!')
                    print()
                else:
                    contactBook.clear()
                    print('Contact-book cleared successfully!')
                    print()
    proceed=input('Show menu?(y/n): ')  
    while proceed not in list(('y','n')):
        proceed=input("Enter only 'y' or 'n': ")
    print()             
        
                    