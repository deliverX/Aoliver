import time
local = time.strftime("%Y-%m-%d %H:%M:%S")
thistime = time.localtime(time.time())
year = thistime.tm_year
which_day_in_year = thistime.tm_yday
print (year,which_day_in_year)
print (local,time.time())
print (thistime)
