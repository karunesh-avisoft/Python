# ------STUDENT MANAGEMENT SYSTEM------

print('------STUDENT MANAGEMENT SYSTEM------')

students=['karunesh']
grades=['A']

proceed='y'
while proceed=='y':
    print('''Select any operation>>>
    1. Add new student
    2. Update grades
    3. Remove Student
    4. Display students''')
    
    choice=int(input('Enter your choice:'))
    
    if choice not in range(1,5):
        print('Wrong Choice!!')
        
    elif choice==4:                  # Display
        if not len(students):
            print('Sorry, no student exits!!')
        else:
            print("STUDENT'S      GRADE'S")
            for idx in range(len(students)):
                print(f'{students[idx]}         {grades[idx]}')
    else:
        name=input('Enter student name:')   # name input
        exists=True if name in students else False  # duolicate student check
        
        if choice==3:               # Remove
            if not exists:
                print('Student does not exists!!')
            else:
                grades.pop(students.index(name))
                students.remove(name)
                print('Student removed successfully...')
        else:
            grade=input('Enter the grade of the student:')      # grade input
            if grade in ('A','B','C','D','E','F','G'):      # invakid grade check
                if choice==1:
                    if exists:
                        print('Student already exists!!')
                    else:
                        students.append(name)
                        grades.append(grade)
                        print('Student added successfully...')
                elif choice==2:
                    if not exists:
                        print('Student does not exists!!')
                    else:
                        grades[students.index(name)]=grade
                        print('Marks updated successfully...')
            else:
                print('Invalid grade entered!!')
           
    proceed=input('Want to proceed(y/n)?')
        
    
    
