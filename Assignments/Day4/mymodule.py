import datetime as dt
import random
    # calculate the age
def calculate_age(birthYear):
    age=dt.datetime.now().year-birthYear
    return age

    # person details
def person_detail(name,birth_year):
    age=calculate_age(birth_year)
    print(f'Hii! {name} you are {age} year old.')

    # default constructor message
def message(msg,lvl='INFO'):
    print(f'{lvl}:{msg}')

    # returns 6 digit OTP
def generate_otp():
    return random.randint(100000,999999)

    # calculate the discount price
def calculate_dis():
    price=int(input('Enter the price of the Item:'))
    dis_rate=int(input('Enter the discount rate:'))
    return price-(price*dis_rate/100)

    # convert celsius to fahrenheit using lambda
def cel_to_fahrenheit(cel:list):
    fahrenheit=map(lambda x:x*9//5+32,cel)
    print('Fahrenheit:',list(fahrenheit))

