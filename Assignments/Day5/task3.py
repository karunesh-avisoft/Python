from pathlib import Path
import json
import csv

# work with a json file
directory=Path('C:/Users/hp/Documents/Python/Assignments/Day5')  #object creation
inp_file=directory/'employees.csv'
op_file=directory/"employees.json"

# write
data={'employees':[]}
print('Data format:', data)
with open(inp_file) as infile, op_file.open('w') as outfile:
    # reader=csv.reader(infile)
    # we can use DictReader() to dorectly convert it to dictionary item
    
    reader=csv.DictReader(infile)
    for line in reader:
        # if len(line)==3:
        # name,dept,salary=[*line]
        # data['employees'].append({'name':name,'departemnt':dept,'salary':salary})
            
        data['employees'].append(line)
    json.dump(data,outfile, indent=4)   # proper spacing
    print('JSON file created!')
    print(json.dumps(data, indent=4))


