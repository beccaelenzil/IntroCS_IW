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
low=int(low)
high1='false'
high='false'
while high1.isdigit()==False or high<=low:
    try:
        high=raw_input('What is the high for "m" and "b"?')
        high=int(high)
        high1=abs(high)
        high1=str(high1)
    except:
        pass
high=int(high)
a=random.randint(low,high)
b=random.randint(low,high)
a=int(a)
b=int(b)
print 'The goal of the game is to guess the equation.'
print 'The equation is y=mx+b where m is between',low,'and',high,'.'
print a
print b
a1='test'
b1='test'
count=-1
guesses=[]
while a1!=a and b1!=b:
    print
    x='test'
    a1='test'
    b1='test'
    x1='false'
    x='false'
    while x1.isdigit()==False:
        try:
            x=raw_input('Input please:')
            x=int(x)
            x1=abs(x)
            x1=str(x1)
        except:
            pass
    x=int(x)
    y=a*x+b
    apen=str(x)+' -> '+str(y)
    guesses.append(apen)
    print guesses
#    print x,'->',y
    a11='false'
    a1='false'
    while a11.isdigit()==False:
        try:
            a1=raw_input('What is "a"?')
            a1=int(a1)
            a11=abs(a1)
            a11=str(a11)
        except:
            pass
    a1=int(a1)
    b11='false'
    b1='false'
    while b11.isdigit()==False:
        try:
            b1=raw_input('What is "b"?')
            b1=int(b1)
            b11=abs(b1)
            b11=str(b11)
        except:
            pass
    b1=int(b1)
    count+=1
print 'Correct. Number of incorrect guesses:',count
