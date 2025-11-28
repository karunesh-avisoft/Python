from regularExpressions import *

def main():
    print("\n=========== REGULAR EXPRESSIONS ===========")
    print("Let's learn some data processing using 'RegEx'.")
    print("===== ACTION'S MENU =====")
    print("1. Word Presence Checker")
    print("2. Number Extraction from Text")
    print("3. Extract Structured Patterns")
    print("4. Clean Up Messy Text")
    print("5. Email Format Validator")
    print("6. Exit")
    print("=" * 40)
    
    choice=input('Enter your choice: ').strip()
    while int(choice) not in range(1,7):
        choice=input('\tEnter your choice again from menu: ').strip()
    match(choice):
        case '1':
            word_checker()
        case '2':
            number_extractor()
        case '3':
            subtracted_patterns()
        case '4':
            text_cleaner()
        case '5':
            email_validator()
        case '6':
            print('\t__GOOD-BYE__')
    
consent='y'
while consent.lower()=='y':
    main()
    consent=input('\nDo you want re-execution?(y/n): ')

