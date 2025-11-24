import csv 

with open('users.csv','w') as file:
    writer=csv.writer(file)
    writer.writerows([['name','age'],["Sam",20],["Rita",30],["John",40]])
    
with open('users.csv','r') as file:
    reader = csv.reader(file)
    res=[]
    for row in reader:
        if len(row)>0 and row[1]!='age' and int(row[1])>25:
            res.append(row[0])
    print('res: ',res)