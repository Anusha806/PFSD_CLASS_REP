'''
import datetime
import time
print(time.time())
print(time.asctime())

anusha=datetime.datetime.now()
print(anusha)
print("Year:",anusha.year)
print("Month:",anusha.month)
print("Hour:",anusha.hour)
print("Minute:",anusha.minute)
print("Second:",anusha.second)
print("Microsecond:",anusha.microsecond)


import calendar
s=calendar.prcal(3023)
s2=calendar.month(2005,2)
s1=calendar.isleap(2005)
print(s1)
print(s2)


x=datetime.datetime.now()
from datetime import timedelta
print(x+timedelta(days=-89))
'''
import time
from datetime import datetime
import pytz
time1=pytz.timezone('Japan')
print("Currenttime is : ", datetime.now(time1))