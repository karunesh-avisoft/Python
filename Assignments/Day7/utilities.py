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


