from datetime import datetime as dt

date=dt.today().date()
time=dt.today().time()

print('Current date:',date)
print('Current time:',time)

# two date difference
def date_diff(date1,date2,fmt='%Y-%m-%d'):
    d1=dt.strptime(date1,fmt).date()
    d2=dt.strptime(date2,fmt).date()
    return abs(d2-d1)

difference=date_diff('2025-11-25','2025-11-11')
print('Date difference:',difference)