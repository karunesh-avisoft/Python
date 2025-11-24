# task1
with open('qa_notes.txt','w') as file:
    file.writelines(['QA refes Quality Assurance\n','Python\n','Playwright\n'])

with open('qa_notes.txt','r') as file:
    print('Content: ',file.read())
    file.seek(0)
    # count=0
    # for line in file:
    #     count+=1
    count=sum(1 for line in file)
    print('Line count: ',count)

# task2
with open('results.log','w+') as file:
    file.write("Test1: PASS\n")
    file.write("Test2: FAIL\n")
    file.write("Test3: FAIL\n")
    file.write("Test4: PASS\n")
    print('Results')
    file.seek(0)        # pointer restfrom the end of the file
    for line in file:
        print(line)
        
