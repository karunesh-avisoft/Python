class Temperature:
    def __init__(self,celsius):
        self.__celsius=celsius
    
    @property   # create a method behave like attribute
    def fahrenheit(self):
        return self.__celsius*9/5+32

t1=Temperature(100)
# print('Fahrenheit:',t1.fahrenheit()) -> TypeError: 'float' object is not callable
print("Fahrenheit:",t1.fahrenheit)