#!/usr/bin/env python
from math import floor

# http://lifehacker.com/5848651/how-to-quickly-figure-out-the-day-of-the-week-any-date-falls-on
# http://www.terra.es/personal2/grimmer/

def whatday(year,month,day):
    mod = 0
    month_code = [0,6,2,2,5,0,3,5,1,4,6,2,4]
    a = int(str(year)[2:])
    a = int(floor(a * 1.25))
     
    if year >= 1900 and year < 2000:
        mod = mod + 1
    
    if (year % 4 == 0) and ((month == 1) or (month == 2)) and (year != 1900):
        mod = mod - 1
    
    if (a + month_code[month] + day + mod) < 0:
        print "Uh oh..."
    return (a + month_code[month] + day + mod) % 7
    
sundays = 0


for year in range(1900,2001):
    for month in range(1,13):
        if whatday(year,month,1) == 0:
            sundays = sundays + 1
            
print sundays