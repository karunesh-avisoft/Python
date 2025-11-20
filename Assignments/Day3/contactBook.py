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
while proceed=='y':
    print('***ACTIONS MENU***')
    print('''    1. All contacts
    2. Search
    3. Add new contact
    4. Update contact
    5. Delete contact''')
    print()
    choice=eval(input('Enter your action:'))
    print()
    
    
    if choice not in range(1,6):
        print('Invalid Action!!')
        print()
    else:
        isEmpty=True if not len(contactBook) else False  # len return 0 if empty
        
        match choice:
            case 1:     # display all contacts
                if not isEmpty:
                    print('\tAll contacts:')
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
                    print()
                    choiceSearch=eval(input('Enter search choice:'))
                    print()
                    if choiceSearch not in range(1,3):
                        print('Invalid search choice!!')
                        print()
                    elif choiceSearch==1:
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
                            print()
                    city=input('Enter city of the person:')
                    print()
                    
                    contactBook[name.capitalize()]={'phone':phone, 'email':email, 'city':city}
                    print('Contact updated successfully!')
                    print()
            case 5:     # delete logic
                name=input('Enter contact name you want to delete:')
                print()
                if name not in contactBook.keys():
                    print('Contact does not exists!!')
                    print()
                else:
                    contactBook.pop(name)
                    print(f'{name} deleted succefully!')
                    print()
    
    proceed=input('Show menu?(y/n):')  
    print()             
        
                    