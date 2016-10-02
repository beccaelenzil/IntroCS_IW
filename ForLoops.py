#1a
def power(b,p):
#b=base, p=exponent
    result = 1
    for x in range(p):
        result *=b
    return result
print "power(2,5): should be 32 == ", power(2,5)
print "power(5,2): should be 25 == ", power(5,2)
print "power(42,0): should be 1 == ", power(42,0)
print "power(0,42): should be 0 == ", power(0,42)
print "power(0,0): should be 1 == ", power(0,0)

#1b
def summedOdds( L ):
    """ loop-based function to return a numeric list, summed odd numbers
        (sum is built-in, so we're using a different name)
        input: L, a list of integers
        output: the sum of the list L
    """
    result = 0
    y=0
    for e in L:
        if L[y]%2 != 0:
            result += L[y]
            y += 1
        else:
            y+=1
    return result

# tests!
print "summedOdds( [4,5,6] ): should be 5 == ", summedOdds( [4,5,6] )
print "summedOdds( range(3,10) ): should be 24 == ", summedOdds( range(3,10) )


def mult(m,n):
    result = 0
    if m>=0 and n>=0 or m<=0 and n<=0:
        p=''
    else:
        p='-'
    m=abs(m)
    n=abs(n)
    for a in range(n):
        result +=m
    result= str(p)+str(result)
    int(result)
    return result
print "mult(6,7)    42 ==", mult(6,7)
print "mult(6,-7)  -42 ==", mult(6,-7)
print "mult(-6,7)  -42 ==", mult(-6,7)
print "mult(-6,-7)  42 ==", mult(-6,-7)
print "mult(6,0)     0 ==", mult(6,0)
print "mult(0,7)     0 ==", mult(0,7)
print "mult(0,0)     0 ==", mult(0,0)

def dot(L,K):
    result = 0
    if len(L) != len(K):
        return int(0)
    elif len(L)==0:
        return int(0)
    else:
        for i in range(len(L)):
            result += L[i]*K[i]
        return result
print "dot( [5,3], [6,4] )     42.0 ==", dot( [5,3], [6,4] )
print "dot( [1,2,3,4], [10,100,1000,10000] )  43210.0 ==", dot( [1,2,3,4], [10,100,1000,10000] )
print "dot( [5,3], [6] )        0.0 ==", dot( [5,3], [6] )
print "dot( [], [6] )           0.0 ==", dot( [], [6] )
print "dot( [], [] )            0.0 ==", dot( [], [] )
