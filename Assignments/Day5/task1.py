from pathlib import Path

# work with a text file
directory=Path('C:/Users/hp/Documents/Python/Assignments/Day5')  #object creation
filepath=directory/"employees.txt"

data=['Karunesh\t','IT\n','Ritik\t','Product\n','Harshit\t','Marketing\n','Harish\t','Sales\n','Naina\t','Audit\n']

with filepath.open('w') as file:
    file.writelines(data)
    print('File created!')

# read with read()
print("Reading with read() function>>")

with filepath.open('r') as file:
    content=file.read()
    print('Content: ',content)
    
# read with readlines()
print("Reading with readlines() function>>")

with filepath.open('r') as file:
    for line in file.readlines():
        print(line)
        
# add using append mode
with filepath.open('a+') as file:
    file.writelines(['Jacob\t','Finance\n'])
    file.seek(0)        # resetting pointer
    print('Data: \n',file.read())