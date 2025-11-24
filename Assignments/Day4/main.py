import mymodule
from mymodule import message
from mymodule import cel_to_fahrenheit as temp_converter

# default constructor
message('User logged in!')
message('User not authenticated!!','WARNING')

# 6 digit otp
otp=000000
def fetch_otp():
    global otp
    otp=mymodule.generate_otp()
fetch_otp()    
print('Your otp is: ',otp)

# discount price
print('To calculate the discount on the item:')
discounted_price=mymodule.calculate_dis()
print('Discounted price is: ',discounted_price)

# celsius to fahrenheit
celsius=[10,25,35,48,50]    # Fahrenheit: [50, 77, 95, 118, 122]
temp_converter(celsius)

# person details
mymodule.person_detail('Abhishek', 2004)