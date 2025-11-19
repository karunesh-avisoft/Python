# remove duplicates

items=['a','b','a','c','d','b','e']
seen=set()
# unique=[x for x in items if not(x in seen or seen.add(x))]
unique=[]

for x in items:
    if x not in seen:
        unique.append(x)
        seen.add(x)

print('Items:',items)
print('Unique:',unique)