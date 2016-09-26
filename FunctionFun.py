#function fun arithmatic proccesing
def tpl(x):
  """
  output: tpl returns thrice its input
  input x: a number (int or float)
  """
  return 3*x
print 'tpl(3) is', tpl(3)

def sq(x):
    """square x"""
    return x*x
print 'sq(2) is', sq(2)

def interp(low,high,fraction):
    """takes in three numbers, low, hi, and fraction, and
    should return the floating-point value that is fraction of the way
    between low and hi."""
    return (high-low)*fraction+low
print 'interp(1,9,.25) is', interp(1,9,.25)
#string functions
def checkends(s):
    """takes in a string s and returns True if the first character in s
    is the same as the last character in s. It returns False otherwise. """
    if s[0] == s[-1]:
        return 'true'
    else:
        return 'false'
print 'checkends (true) is', checkends('true')

def flipside(s):
    """takes in a string s and returns a string whose first half is s's
    second half and whose second half is s's first half."""
    z = len(s)/2
    return s[z::]+s[0:z]
print 'flipside(carpets) is', flipside('carpets')

def convertFromSeconds( s ):
# I think your math is wrong for 100000 in trinket
    days = s / (24*60*60)  # # of days
    s = s % (24*60*60)     # the leftover
    hours = s / (60*60)    # # of hours
    s = s % (60*60)        # the leftover
    minutes = s % (60)     # # of minutes
    s = s % (60)           # the leftover
    seconds = s            # # of seconds
    return [days, hours, minutes, seconds]
print 'convertFromSeconds(86400)', convertFromSeconds(86400)

def front3(string):
    return string[0:3]*3
print 'front3(java) is',front3('java')
