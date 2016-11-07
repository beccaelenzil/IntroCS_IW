import sys;
print (sys.version)
import time
import calendar
import random
def randomgendergroups():
    x=raw_input('how many times?')
    x=int(x)
    t=0
    u=0
    st=time.gmtime()
    st=calendar.timegm(st)
    for i in range (x):
        a=2
        p1=random.randint(0,1)
        p2=random.randint(0,2)
        if p1==p2:
            t+=1
        else:
            u+=1
    print 'number of seconds needed to calculate:',calendar.timegm(time.gmtime())-st
    print 'same gender groups =',t,'/',x
    print 'defrent gender groups =',u,'/',x
    print 'ration of same gender groups to different gender groups is:',float(t)/x,':',float(u)/x

listtest=[1,2,3,4,5,6,7,8,9,10]
listtest=random.sample(listtest,len(listtest))
print listtest

w=10
h=10
var1=10 #number of variable one in board
var2=10 #number of variable two on the board
var3=(w*h)-(var1-var2)
assignlist=var1*['A']+var2*['B']+var3*[' ']
assignlist1=random.sample(assignlist,len(assignlist))
print assignlist1
