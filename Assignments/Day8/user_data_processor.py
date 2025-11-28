from custom_exception import *
from pathlib import Path

def main():
    # user detail    
    print(f'\n========== EXCEPTION HANDLING ==========')
    # validity variables
    valid_name=valid_age=valid_fav=valid_file=False
    summary={"content":None}
    print('    ____User Details____')
    try:
        # name exception
        name=input('Enter your name: ').strip()
        try:
            if not all(ch.isalpha() or ch in ", -'" for ch in name) or name=='':
                raise ValueError("Name can't include special caracters, digits or empty string!!")            
        except ValueError as e:
            print('\tValueError:',e)
        else:
            print(f'\tHellooo! Mr/Mrs {name.title()}.')
            valid_name=True
            summary['name']=name.title()
        
        # age exception 
        age=input('\nEnter your age: ').strip()
        try: 
            age=int(age)
            if age<0:
                # custom 1
                raise NegativeAgeError('Can not enter negative age!')
            if age<18:
                # custom 2
                raise InvalidAgeError('You are not allowed to vote!!')
        except InvalidAgeError as e:
            print('\tInvalidAgeException:',e)
        except NegativeAgeError as e:
            print('\tNegativeAgeError:',e)
        except ValueError as e:
            print('\tValueError:Invalid value entered for age!!')
        else:
            print('\tExcellent, You are eligible to contribute your vote!')
            valid_age=True
            summary['age']=age
        
        # favourite number exception
        fav_number=input('\nEnter your favourite number less than 100: ').strip()
        try:
            fav_number=int(fav_number)
            # custom 2
            if fav_number<0 or fav_number>100:
                raise FavouriteNumberException
        except FavouriteNumberException as e:
            e.message('Your favourite number can neither be negative nor more than 100.')
        except ValueError as e:
            print('\tValueError:Invalid value entered for favourite number!!')
        else:
            print(f'\tYour favourite number is {fav_number}')
            valid_fav=True
            summary['fav']=fav_number
        
        # safe division
        if valid_fav:
            print("-" * 40)
            res=0
            try:
                res=100/fav_number
            except ZeroDivisionError:
                print('\tDivisionByZeroError:Aa Aaa...division by 0 gives you infinity!')
            except TypeError:
                print('\tTypeError:Favourite number has different data type!!')
            else:
                print(f'\tYeahh! Safe division was successfull with result {res:.2f}')
                summary['div']=res
            
        print("-" * 40)
        
        # file handling exception
        directory=Path('C:/Users/hp/Documents/Python/Assignments/Day8')  #object creation
        file_name=input('\nEnter a file name: ').strip().lower()
        filepath=directory/file_name
        try:
            with open(filepath,'r') as file:
                content=file.read()
                print(f'\n____Content from {file_name}____\n')
                print(content)
                valid_file=True
                summary['content']=content
        except FileNotFoundError:
            print('\tFileNotFoundError:File does not exists!!')
        except PermissionError:
            print('\tPermissionError:You do not have required permission!!')
        finally:
            print(f'\nFinally:File operation is complete, regardless of success or failure.')
            
    # common exception
    except KeyboardInterrupt:
        print('\tKeyboardInterrupt:This was a keybord interruption!!')
    except EOFError:
        print('\tEOFError:Detected end-of-file command!!')   
    else:
        print("-" * 40)
        
        # summary
        print("\n============= SUMMARY =============")
    
        if valid_name:
            print(f"Name               : {summary['name']}")
        if valid_age:
            print(f"Age                : {summary['age']}")
        if valid_fav:
            print(f"Favourite Number   : {summary['fav']}")
        if "div" in summary.keys():
            print(f"Division Result    : {summary['div']}")
        if summary["content"] is not None:
            print("\nFile Content:\n")
            print(summary["content"])

    print("\n=======================================\n")
 
main()       
# consent='y'
# while consent.lower()=='y':
#     main()
#     consent=input('Do you want to re-execute the program?(y/n): ').strip()