import sys;
print (sys.version)

import random
low1='false'
low='false'
while low1.isdigit()==False:
    try:
        low=raw_input('What is the low for "m" and "b"?')
        low=int(low)
        low1=abs(low)
        low1=str(low1)
    except:
        pass

print low
print low1
