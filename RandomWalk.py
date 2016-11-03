import random
def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])
def rwPos(start,nsteps):
    currentPosition=start
    for i in range(0, nsteps):
        currentPosition=currentPosition+rs()
        print 'currentPosition is', str(currentPosition)
    return currentPosition
def rwsteps( start, low, hi ):
    y=0
    start1=start
    while start!=low and start!=hi:
        disp='|'+' '*(hi-low)+'|'
        disp=disp[0:start-1]+'S'+disp[start+1::]
        print disp
        start=start+rs()
        y+=1
    omega=['number of steps=',y,'signed displacment=',start-start1,'squared-displacement',(start-start1)**2]
    return omega
#signed displacment: it's the ending position of the random walker
# minus the starting position of the random walker

rwsteps(5,0,10)

def rwposPlain(start,nsteps):
    y=0
    start1=float(start)
    for i in range (nsteps):
        start=start+rs()
        y+=1
    omega=[y,start1-start,(start1-start)**2]
    return omega

def ave_signed_displacement(numtrials):
    total=0
    for i in range(numtrials):
        total+=rwposPlain(0,100)[1]
    return total/numtrials

def ave_squared_displacement(numtrials):
    total=0
    for i in range(numtrials):
        total+=rwposPlain(0,100)[2]
    return total/numtrials
#print rwsteps(5,0,10)

testnum=raw_input('Number of Tests:')
testnum=int(testnum)
print 'average signed displacment is',ave_signed_displacement(testnum)
print 'average squared displacment is',ave_squared_displacement(testnum)

"""
explanation:
   In order to compute the average signed displacement for
   a random walker after 100 random steps, I
   ran rwpos(0,100) numtrials times and had a variable total
   that was equal to the sum.  I then divided total by numtrials
   it averages to around 0
   to compute squared displacement i used a copy of average_signed_displacement
   except a had the variable it pulled out of rwposPlain be squared displacement
   it averages to around 100
one example of data:
   average signed displacment is -1
   average squared displacment is 122
"""
