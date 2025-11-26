# Parent class to provide a template for courses
class Course:
    platform='EduConnect'   # class variable
    def __init__(self,course_code,course_name,instructor,duration):
        # instance variables
        self.course_code=course_code
        self.course_name=course_name
        self.instructor=instructor
        self.duration=duration
        print(f'\nCourse_Code:{self.course_code} created successfully!\n')
         
    def display_details(self):
        print('\n____Course Details____')
        print('Course Code: ',self.course_code)
        print('Course Name: ',self.course_name)
        print('Instructor: ',self.instructor)
        print(f'Duration: {self.duration}hr')
    
    def update_courseName(self,newName):
        self.course_name=newName
        print(f'\tSuccess:{self.course_code} Course name updated to {self.course_name}.')
    def update_instructor(self,newInstructor):
        self.instructor=newInstructor
        print(f'\tSuccess:{self.course_code} Instructor name updated to {self.instructor}.')
    def update_duration(self,newDuration):
        self.duration=newDuration
        print(f'\tSuccess:{self.course_code} Duration updated to {self.duration}.')
        
# Child class ProgrammingCourse
class ProgrammingCourse(Course):
    def __init__(self,course_code,course_name,instructor,duration,language,real_projects):
        super().__init__(course_code,course_name,instructor,duration)   # parent constructor call
        self.language=language              # instance variable
        self.real_projects=real_projects    # instance variable
        self.category='Programming'
        
    def display_details(self):
        print(f"\n===== {self.platform} =====")     # shared variable
        super().display_details()   # parent function call
        print('Language: ',self.language)
        print('Real World Projects: ',self.real_projects)
        print(f'Category: {self.category}')
        print()
        
# Child class DesignCourse
class DesignCourse(Course):
    def __init__(self,course_code,course_name, instructor, duration,tool_used,lectures):
        super().__init__(course_code,course_name, instructor, duration)   # parent constructor call
        self.tool_used=tool_used    # instance variable
        self.lectures=lectures      # instance variable
        self.category='Design'
        
    def display_details(self):
        print(f"\n===== {self.platform} =====")     # shared variable
        super().display_details()   # parent function call
        print('\tTool Used: ',self.tool_used)
        print('\tTotal Lectures: ',self.lectures)
        print(f'\tCategory: {self.category}')
        print()
        
# Demonstration
courses={}
# programming courses
courses[101]=ProgrammingCourse(101,'Programming in Java','Tim Buchaka',60,'English',10)
courses[102]=ProgrammingCourse(102,'Programming in Python','Hitesh Chowdhary',60,'Hindi',12)
# design courses
courses[103]=DesignCourse(103,'UI/UX Designing','Bhawana',55,'Figma',22)

# utility methods
def inputCode():
    course_code=input('\nEnter course code: ')
    while not course_code.isdigit():
        course_code=input('Enter a valid course code: ')
    return int(course_code)

def inputName():
    course_name=input('\nEnter the name of the course: ')
    while course_name.isdigit():
        course_name=input('Enter a valid name of the course: ')
    return course_name

def inputInstructor():
    instructor=input('\nEnter the instructor name: ')
    while instructor.isdigit():
        instructor=input('Enter a valid instructor name: ')
    return instructor

def inputDuration():
    duration=input('\nEnter the duration(hr): ')
    while not duration.isdigit():
        duration=input('Enter the duration in hours: ')
    return int(duration)

def inputLanguage():
    language=input('\nEnter the language of the course: ')
    while language.isdigit():
        language=input('Enter a valid language for course: ')
    return language

def inputProjects():
    real_projects=input('\nEnter the duration(hr): ')
    while not real_projects.isdigit():
        real_projects=input('Enter the duration in hours: ')
    return int(real_projects)

def inputTool():
    tool_used=input('\nEnter the tool used: ')
    while tool_used.isdigit():
        tool_used=input('Enter a valid tool used: ')
    return tool_used

def inputLectures():
    lectures=input('\nEnter the number of lectures: ')
    while not lectures.isdigit():
        lectures=input('Enter a valid number of lectures: ')
    return int(lectures)

def list_res(codes):
    w_code = 15
    w_name = 30
    w_inst = 20
    w_dur = 15
    print("=" * 100)
    print(f'{"Course Code":<{w_code}}'
          f'{"Course Name":<{w_name}}'
          f'{"Instructor":<{w_inst}}'
          f'{"Duration(hr)":<{w_dur}}'
          f'{"Category"}')
    print("-" * 100)
    for key in codes:
        print(f'{courses[key].course_code:<{w_code}}'
              f'{courses[key].course_name:<{w_name}}'
              f'{courses[key].instructor:<{w_inst}}'
              f'{courses[key].duration:<{w_dur}}'
              f'{courses[key].category}')
    print("=" * 100)

consent='y'
while consent.lower()=='y':
    print("\n===== ONLINE COURSE SYSTEM MENU =====")
    print("1. Add new course")
    print("2. Edit course")
    print("3. Search course")
    print("4. Delete course")
    print("5. Display all course")
    print("6. Exit")
    print("=" * 40)
    
    choice = input("Enter your choice: ")
    while not choice.isdigit() or int(choice) not in range(1,7):
        choice=input("Enter a valid choice of operation: ")
    # Add new course
    if choice == '1':
        # category
        category=input('\nEnter the category of the course programming/design: ')
        while category.isdigit():
            category=input('\tEnter the category of the course programming/design: ')
        # course code
        course_code=inputCode();
        if course_code in courses:      # does exists?
            print(f'\nCourse with course code "{course_code}" already exists!!')
        else:
            # course name
            course_name=inputName()
            # instructor name
            instructor=inputInstructor()
            # duration
            duration=inputDuration()
            # programming course
            if category=='programming':
                # language
                language=inputLanguage()
                # real world projects
                real_projects=inputProjects()
                # store object
                courses[course_code]=ProgrammingCourse(course_code,course_name,instructor,duration,language,real_projects)
            # design course
            elif category=='design':
                # language
                tool_used=inputTool()
                # real world projects
                lectures=inputLectures()
                # store object
                courses[course_code]=DesignCourse(course_code,course_name,instructor,duration,tool_used,lectures)
    # edit course
    elif choice=='2':
        # course code
        course_code=inputCode();
        if course_code not in courses:      # does exists?
            print(f'\nCourse with course code {course_code} does not exists!!')
        else:
            print("\n---- Edit by? ----")
            print("\t1. Course name")
            print("\t2. Instructor")
            print("\t3. Duration")
            print("\t4. Exit")
            print("-" * 30)
            
            editChoice=input('Enter your edit choice: ')
            while int(editChoice) not in range(1,5):
                editChoice=input('Enter your valid edit choice: ')
            obj=courses[course_code]
            if editChoice=='4':
                print(f'\tExit from {course_code} edit!')
            elif editChoice=="1":
                course_name=inputName()
                obj.update_courseName(course_name)
            elif editChoice=="2":
                instuctor=inputInstructor()
                obj.update_instructor(instuctor)
            elif editChoice=="3":
                duration=inputDuration()
                obj.update_duration(duration)
    # search
    elif choice=='3':
        print("\n---- Search by? ----")
        print("1. Course code")
        print("2. Instructor")
        print("3. Category")
        print("4. Exit")
        print("-" * 20)
        
        searchChoice=input('Enter your search choice: ')
        while not searchChoice.isdigit() or int(searchChoice) not in range(1,5):
            searchChoice=input('Enter your valid search choice: ')
            
        if searchChoice=='4':
            print(f'\tExit from search menu!')
        elif searchChoice=='1':
            course_code=inputCode()
            if course_code in courses:
                courses[course_code].display_details()      # object retrieval to call methods
            else:
                print(f'Course with course code {course_code} does not exists!!')
        elif searchChoice=='2':
            inst=inputInstructor().strip().lower()
            codes=[]    # to store the course codes
            for key in courses.keys():
                if inst in courses[key].instructor.lower():
                    codes.append(key)
            if len(codes)==0:
                print(f'\tSorry no course exists of instructor "{inst}"!!')
            else:
                list_res(codes)
        elif searchChoice=='3':
            categ=input('\nEnter the category of the course programming/design: ')
            while categ.isdigit():
                categ=input('Enter the category of the course programming/design: ')
            codes=[]
            categ=categ.strip().lower()
            for key in courses.keys():
                if categ in courses[key].category.lower():
                    codes.append(key)
            if len(codes)==0:
                print(f'\tSorry no course exists with category "{categ}"!!')
            else:
                list_res(codes)
    # delete course
    elif choice=='4':
        course_code=inputCode()
        if course_code in courses:
            del courses[course_code]
            print(f'\n\tCourse:{course_code} deleted successfully!')
        else:
            print(f'Course with course code "{course_code}" does not exists!!')
    # display all
    elif choice=='5':
        list_res(courses.keys())
    # exit from main menu
    elif choice=='6':
        print(f'\n\tThankyou for choosing {Course.platform}. See you soon...')

    consent=input('\nStill you want to explore?(y/n): ')
    while consent.isdigit():
        consent=input('\nDo you still want to explore?(y/n); ')       
            
