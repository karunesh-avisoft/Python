class Car:
    brand=None
    model=None
    year=None
    
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def display(self):
        print('Brand:',self.brand)
        print('Model:',self.model)
        print('Year:',self.year)
        
    def update_year(self,year):
        self.year=year
    
car1=Car('Tata','Nexon','2025')
car1.display()
car1.update_year(2026)
print('Updated year:',car1.year)