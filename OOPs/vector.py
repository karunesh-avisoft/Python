# OPERATOR OVERLOADING
class Vector:
    # MAGIC/DUNDER/SPECIAL FUNCTIONS
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def __add__(self,other):
        self.a+=other.a
        self.b+=other.b
        return Vector(self.a,self.b)
    
    def __str__(self):
        return f'({self.a},{self.b})'
        
v1=Vector(2,3)
v2=Vector(1,4)
print(v1+v2)