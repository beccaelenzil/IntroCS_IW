
import random
low='false'
while low.isdigit()==False:
    low=raw_input('What is the low for "m" and "b"?')
low=int(low)
high='false'
while high.isdigit()==False and high>=low:
    high=raw_input('What is the high for "m" and "b"?')
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
    while x.isdigit()==False:
        x=raw_input('input please:')
    x=int(x)
    y=a*x+b
    apen=str(x)+'->'+str(y)
    guesses.append(apen)
    print guesses
#    print x,'->',y
    while a1.isdigit()==False:
        a1=raw_input('what is m?')
    a1=int(a1)
    while b1.isdigit()==False:
        b1=raw_input('what is b?')
    b1=int(b1)
    count+=1
print 'number of wrong guesses:',count
