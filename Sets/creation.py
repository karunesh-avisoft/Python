# Sets in python

# empty_set=set() # set
# eset={}         # dict
# print(type(empty_set))
# print(type(eset))
demo=set()
demo.add(1)
demo.add(1)  # ignored without any error
demo.add(2)
demo.add((3,4,5,3,5))    # can add only tuple
demo.add(3)
demo.add(4)
demo.add(5)
demo.add(3)
demo.add(5)

# print('Set: ', demo)

demo.remove(3)
# demo.remove(3) will show keyerror

demo.discard(3)     # safe removal

A={1,2,3}
print('A:',A)
B={3,4,5}
print('B:',B)

# union
# C=A.union(B)
C=A|B
print('Union:C ',C)

# intersection
D=A.intersection(C)
E=A&B
print('Intrsection:D ',D)
print('Intrsection:E ',E)

# difference
F=A-B
G=A.symmetric_difference(B)     # remove the elements in both common
print('Difference:F ',F)
print('Symmetric Difference:G ',G)

# is subset
res={2,4}.issubset({1,2,3,4,5})
print('Is subset:',res)

# remove randome pop()
H={10,20,30,40,50}
print('Random ele:',H.pop())
print('Random ele:',H.pop())
print('Random ele:',H.pop())

# combine list to set
list1=[5,6,7]
I={1,2,3,4}
I=I|{*list1}
print('Combines set:',I)

# is distinct
print('Distinct:',{1,2}.isdisjoint({3,4,5}))

#  empty
C.clear()
print('Check empty:',C)

# is superset
I={2,4,6,8}
J={1,2,3,4}
print('Superset')
print('I:',I.issuperset(J))
print('J:',J>=I)