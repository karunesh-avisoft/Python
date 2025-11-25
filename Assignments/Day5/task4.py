from pathlib import Path
import json

# data processing
directory=Path('C:/Users/hp/Documents/Python/Assignments/Day5')  #object creation
filepath=directory/'employees.json'

emp=[]
emp_with_salary={}
with filepath.open('r') as file:
    data = json.load(file)
    for employee in data['employees']:
        if int(employee['Salary'])>40000:
            emp.append(employee['Name'])
            emp_with_salary.update({employee['Name']:int(employee['Salary'])})
            
print('Employees: ', emp)
print('Employees with salary: ')
w_name=10
print(f'{"Name":<{w_name}} Salary')
print(f'{"____":<{w_name}} ______')
for name,salary in emp_with_salary.items():
    print(f'{name:<{w_name}} {salary}')