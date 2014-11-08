#day of the year

month = raw_input('Please give the numerical representation of the month')
day = raw_input('Please give the day of the month')

short_months = [ 4, 6, 9, 11]
long_months = [ 1, 3, 5, 7, 8, 10, 12]

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
while not is_number(month):
    month = raw_input('Please give the numerical representation of the month')
while not is_number(day) :
    day = raw_input('Please give the day of the month')
day = int(day)
month = int(month)

if month in  short_months :
    while day < 1 and day > 30 :
        day = int(raw_input('Please give the day of the month'))
        while not is_number(day) :
            day = int(raw_input('Please give the day of the month'))
elif month == 2 :
    while day < 1 and day > 28 :
        day = int(raw_input('Please give the day of the month'))

elif month in  long_months :
    while day < 1 and day > 31 :
        day = int(raw_input('Please give the day of the month'))
        while not is_number(day) :
            day = int(raw_input('Please give the day of the month'))
        
if month >=1 and month <=2 :
    return day
if month > 2 and month <= 4 :
    return (month * 31 - 3)
if month > 4 and month <= 6 :
   return (month * 31 - 4)
if month > 6 and month <= 9 :
    return (month * 31 - 5)
if month > 9 and month <=11:
    return (month * 31 - 6)
if month > 11 and month <= 12 :
    return (month * 31 - 7)
elif month > 12 or month < 1 :
    return ' ERROR IN MONTH INPUT'
