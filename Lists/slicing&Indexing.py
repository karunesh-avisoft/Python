letters = ['a','b','c','d','e','f','g','h','i','j']
print('First 5:',letters[:5])
print('Last 4:',letters[-4:])
print('From 2 to 7:',letters[2:8])
print('Every second letter:',letters[0::2])
print('Reverse using slicing:',letters[::-1])


# ######################
nums=list(range(1,21))
print('Nums:',nums)

# even numbers
even=nums[1::2]
print('Even nums:',even)

# multiple of 3
multiples=nums[2::3]
print('Multiples of 3:',multiples)

# 10 - 15
range=nums[9:15]
print('Nums from 10 to 15',range)

# reversed
reversed=nums[::-1]
print('Reversed nums:',reversed)


# #########################
data=[1,2,3,4,5,6,7,8,9,10]
print('Data:',data)

data[3:6]=[99,99,99]
print('Replaced 3 to 6:',data)

data[0::2]=[0]*len(data[0::2])  # len fn counts the total number of zeroes required
print('Rplaced every second element:',data)