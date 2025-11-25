from pathlib import Path
import csv
import random

# work with a csv file
directory=Path('C:/Users/hp/Documents/Python/Assignments/Day5')  #object creation
inp_file=directory/'employees.txt'
op_file=directory/"employees.csv"

with open(inp_file) as infile, open(op_file,'w') as opfile:
    writer=csv.writer(opfile)
    writer.writerow(['Name','Department','Salary'])
    
    for line in infile:
        name,department=[x.strip() for x in line.split('\t')]
        salary=random.randint(40000,100000)
        writer.writerow([name,department,salary])
    print('CSV file created!')

w_name = 10
w_dept = 12
w_salary = 10
    
with op_file.open('r') as file:
    reader=csv.reader(file)
    for line in reader:
        if len(line)>0:
            print(f"{line[0]:<{w_name}} {line[1]:<{w_dept}} {line[2]:<{w_salary}}")