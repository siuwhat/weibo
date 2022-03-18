import time

day_dict={
    'Jan':1,
    'Feb':2,
    'Mar':3,
    'Apr':4,
    'May':5,
    'Jun':6,
    'Jul':7,
    'Aug':8,
    'Sep':9,
    'Oct':10,
    'Nov':11,
    'Dec':12
}

class timer():

    def __init__(self,tm_year=0,tm_mon = 0,tm_mday = 0,tm_hour = 0,tm_min  = 0,tm_sec =0):
        self.tm_year=tm_year
        self.tm_mon=tm_mon
        self.tm_mday=tm_mday
        self.tm_hour=tm_hour
        self.tm_min=tm_min
        self.tm_sec=tm_sec
        self.tm_wday = 0
        self.tm_yday = 0
        self.tm_isdst = 0
    def tuple(self):
        return (self.tm_year,self.tm_mon,self.tm_mday,self.tm_hour,self.tm_min,self.tm_sec,self.tm_wday,self.tm_yday,self.tm_isdst)

def TimeFormatTransform(times):
    times=times.split(' ')
    hms=times[-3].split(':')
    mytime=timer(int(times[-1]),day_dict.get(times[1]),int(times[2]),int(hms[0]),int(hms[1]),int(hms[2]))
    return time.strftime("%Y-%m-%d %H:%M:%S",mytime.tuple())