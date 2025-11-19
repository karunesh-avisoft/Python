shopping_list = []
# append
shopping_list.append('milk')
shopping_list.append('bread')
shopping_list.append('eggs')
# extend
shopping_list.extend(('butter','cheese','yogurt'))

print('Final list:',shopping_list)


# insert

planets=['Mars','Jupiter','Saturn','Uranus','Neptune']

planets.insert(1,"Venus")
planets.insert(1,"Earth")

print('Planets:',planets)

# remove,pop & delete

tasks=['email','meeting','lunch','code','review','deploy']
# remove
tasks.remove('lunch')
print('Tasks:',tasks)
# pop
print(tasks.pop(0))
print('Tasks:',tasks)
# del
# del tasks[-2:] delete with slice
del tasks[-2],tasks[-1]
print('Tasks:',tasks)



# sort and reverse
scores=[88,93,75,95,81,90,78]
print('Original:',scores)

# copy method
cpScores = scores.copy()

cpScores.sort()
print('Ascending order:',cpScores)
cpScores.sort(reverse=True)          # reverse
print('Descending order:',cpScores)

scores.reverse()
print('Reversed:',scores)
