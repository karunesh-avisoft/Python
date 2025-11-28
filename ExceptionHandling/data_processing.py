# list cleaner
def clean_number(nums):
    res=[]
    for num in nums:
        try:
            if isinstance(num,str):
                if num.isdigit():
                    res.append(int(num))
                else:
                    pass
            else:
                raise TypeError(nums.index(num))
        except TypeError as e:
            print('Aa Aaa...encountered type error at',e)
    return res

nums=['3','45','wer','.']
nums.append((2,3,4,5))
nums.append({1:'one',10:'ten'})    
            
print(clean_number(nums))

# string processor
def process_string(txt):
    try:
        if not isinstance(txt, str):
            raise TypeError('You must have entered wrong type!')
        print('\t',txt.upper())
    except TypeError as e:
        print('\tTypeError:',e)
    except:
        print('\tProcessing failed.')
process_string('kARu')
process_string(123)
process_string('123')