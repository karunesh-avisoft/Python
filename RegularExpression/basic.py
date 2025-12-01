import re

text1="The Python programming language is popular."
text2="My phone number is 123-456-7890."
text3="abcdefxyz"

x1=re.search("Python",text1)
print(x1.group())   # Python

x2=re.search('\d',text2)
print(x2.group())   # 1

x3=re.findall('[a-f]',text3)
print(x3)   # ['a', 'b', 'c', 'd', 'e', 'f']

# 3 lettered word
sent="He has a cat"
a=re.search('[a-zA-Z]{3}',sent)
print(a.group())    # has

# pattern matching
str1='Hello, how are you?'
str2='Hi there!'
# starts with ^
print(re.findall('^Hello',str1))  # ['Hello']
print(re.findall('^Hello',str2))  # does not []

# ends with $
str3="I am singing and dancing while running."
print(re.findall('ing$',str3))  # [) whole string not ending with ing having fullstop 
print(re.findall(r'\b\w*ing\b',str3))   # ['singing', 'dancing', 'running']

# consecutive vowels
str4='beautiful voice'
print(re.findall('[aeiou]{2}',str4))