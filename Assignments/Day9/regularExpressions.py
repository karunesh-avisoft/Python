import re

# Task 1 - Word Presence Checker
def word_checker():
    print("\n=========== Word Presence Checker ===========")
    sentence=input('Enter any sentence: ').strip()
    word=input('Enter the word to search: ').strip()
    if word=='' or sentence=='':
        print('\tWRONG:You entered wrong input!')
        return    
    # safe search with whole-word boundaries for special chars
    pattern = r'(?<!\w)' + re.escape(word) + r'(?!\w)'
    # this pattern means
    # - the word should not starts or ends with any letter, number and underscore
    
    found=re.search(pattern,sentence)
    if found:
        print(f"\tFOUND:'{word}' exists at {found.span()[0]} in the sentence.")
    else:
        print(f"\tNOTFOUND:'{word}' doesn't exists in the sentence!")
    print('='*50)   
    
# Task 2 — Number Extraction from Text
def number_extractor():
    print("\n=========== Number Extractor ===========")
    # [^a-zA-Z0-9] -> \W non-word chars means special ones
    para=input('Enter a paragraph: ')
    found=re.findall(r'(?<!\S)-?\d+(?!\S)',para)  
    # in this case pattern means the digit should not starts or ends with any non space char
    #  also dealig with start or end of string which restricted by \s
     
    print(f"\tNUMBERS:",found)
    print('='*50)   
      
# Task 3 — Extract Structured Patterns
def subtracted_patterns():
    print("\n=========== Pattern Extractor ===========")
    
    order_details='Order ID: AXT-2025 delivered to warehouse 18'
    
    order_code=re.search(r"[A-Z]{3}-[0-9]{4}",order_details)
    wh_number=re.search(r'warehouse (\d+)',order_details)   # 'warehouse 18'
    # print(type(wh_number.group()))
    print('\tOrder Code:', order_code.group())
    print('\tWarehouse Number:', wh_number.group(1))
    
    print('='*50) 
    
# Task 4 — Clean Up Messy Text
def text_cleaner():
    print("\n=========== Messy Text Cleaner ===========")
    
    text=input('Enter some messy text: ')
    # removed special characters
    text=re.sub(r'[^A-Za-z0-9 ]+', '', text)
    # removed extra space
    text=re.sub('\s+',' ',text)
    # leading space & 
    text=re.sub('^\s+\s+$','',text)
    
    print('\tCLEANED_TEXT:',text)
    print('='*50) 
    
# Task 5 — Basic Email Format Validation
def email_validator():
    print("\n=========== Email Validator ===========")
    
    email=input('Enter an email: ').strip()
    
    if len(re.findall('[@.]',email))>1 and (re.search('^..$',email) and re.search('^[~!@#$%^&*.|\/?]',email)) is None:
        print('\tVALID: E-mail is in the valid format.')
    else:
        print('\tINVALID: E-mail is in invalid format!')
        
    print('='*50) 
