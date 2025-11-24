import os

# with open()
# directory='C:/Users/hp/Documents/Python/FileHandling'
# filename='sample.txt'
# print('Directory:',directory)
# filepath=os.path.join(directory,filename) # joins without / or \ error

# # with open you have to use close()
# # file=open(filepath,'x')
# # file.write('''Karunesh
# #            QA Trainee
# #            Avisoft''')
# # print(file.readline())
# # file.close()

# # use with that automatically closes the file after use
# with open(filepath,'a+') as file:
#     file.write('On an amazing journey to become QA Engineer.')
#     file.seek(0)
#     for line in file.readlines():
#         print('Line: ', line)
    
# with pathlib
# from pathlib import Path

# directory=Path('C:/Users/hp/Documents/Python/FileHandling')
# directory.mkdir(parents=True,exist_ok=True)
# filepath=directory/'example.txt'
# filepath.write_text("Hello, from pathlib!")
# print('File created:', filepath)

# file creation 
# f = open("sample.txt", "w")
# f.write('Hello QA Experts!')
# f.close()

# reading file
# with open("sample.txt","r") as f:
#     print("read(): ",f.read())
    
# with open("sample.txt","r") as f:
#     print("readline(): ",f.readline())

# with open("sample.txt","r") as f:
#     print("readlines(): ",f.readlines())

# cant use all the method at once wtihout resetting it with f.seek(0)

# writing to the file
lines=['Line 1\n', 'Line 2\n']
with open("sample.txt", "a+") as f:
    # f.write('First line\n')
    # f.writelines(lines)
    f.seek(0)
    print(f.read())