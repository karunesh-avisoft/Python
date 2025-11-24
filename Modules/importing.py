import math
from math import pi
import random as r
from datetime import datetime


# squareroot
def calculate_square_root(value):    
    return math.sqrt(value)
print('Square root of 4:',calculate_square_root(4))
# circle area
def calculate_circle_area(radius):
    return pi * radius ** 2 
print('Area of the circle:',calculate_circle_area(3))
# random number
def generate_randnum(start, end):
    return r.randint(start, end)
print('Random number b/w 1 & 100:',generate_randnum(1,100))
# date 
date=datetime.today().day.
time=datetime.today().day

print('Date:',date)
print('Time:',time)
