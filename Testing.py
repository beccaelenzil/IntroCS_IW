import sys;
print (sys.version)
import time
import calendar
import random
x=raw_input('how many times?')
x=int(x)
t=0
u=0
st=time.gmtime()
st=calendar.timegm(st)
for i in range (x):
    a=2
    p1=random.randint(0,1)
    p2=random.randint(0,1)
    if p1==p2:
        t+=1
    else:
        u+=1
print 'number of seconds needed to calculate:',calendar.timegm(time.gmtime())-st
print 'same gender groups =',t,'/',x
print 'defrent gender groups =',u,'/',x
print 'ration of same:',float(t)/x,'different is:',float(u)/x
