class Employee:
    company='Avisoft'
    
    @staticmethod
    def is_office_day(day):
        return True if day in range(1,6) else False
    
    def change_company(self, new_name):
        self.company=new_name

as98=Employee()
print('Company:',as98.company)

print('Is office day:',as98.is_office_day(2))

as98.change_company('Avi Softwares')

print('Company:',as98.company)