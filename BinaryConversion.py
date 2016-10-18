import math
def numToBinary(N):
    if N==0:
        return ''
    elif N%2==1:
        return numToBinary(N/2) +'1'
    else:
        return numToBinary(N/2)+'0'

print 'numToBinary(0)=''=', numToBinary(0)
print 'numToBinary(1)=1=', numToBinary(1)
print 'numToBinary(4)=100=', numToBinary(4)
print 'numToBinary(10)=1010=', numToBinary(10)
print 'numToBinary(42)=101010=', numToBinary(42)
print 'numToBinary(100)=1100100=', numToBinary(100)

def binaryToNum(S):
    y=-1
    return binaryToNum2(S,y)
def binaryToNum2(S,y):
    if S == '':
        return 0
  # if the last digit is a '1'
    elif S[-1] == '1':
        y += 1
        return  binaryToNum2(S[0:-1],y)+math.pow(2,y)
    else: # last digit must be '0'
        y += 1
        return  binaryToNum2(S[0:-1],y)

print 'binaryToNum('')=0=', binaryToNum('')
print 'binaryToNum(1)=1=', binaryToNum('1')
print 'binaryToNum(100)=4=', binaryToNum('100')
print 'binaryToNum(1010)=10=', binaryToNum('1010')
print 'binaryToNum(101010)=42=', binaryToNum('101010')
print 'binaryToNum(1100100)=100=', binaryToNum('1100100')

def increment(S):
    if S=='11111111':
        return '00000000'
    else:
        a=binaryToNum(S)
        a+=1
        a=int(a)
        b=numToBinary(a)
        return '0'*(8-len(b))+b
print 'increment(\'00000000\')->', increment('00000000')
print 'increment(\'00000001\')->', increment('00000001')

def count(S,n):
    print S
    for c in range(n):
        print increment(S)
        S=increment(S)
print 'count(\'00000000\', 4) is'
count('00000000', 4)

print 'count(\'11111110\', 5) is'
count('11111110', 5)

def numToTernary(N):
    if N==0:
        return ''
    elif N%3==2:
        return numToTernary(N/3) +'2'
    elif N%3==1:
        return numToTernary(N/3) +'1'
    else:
        return numToTernary(N/3)+'0'
print numToTernary(42),'should be \'1120\''
print numToTernary(4242),'should be \'12211010\''

def ternaryToNum(N):
    y=-1
    return ternaryToNum2(N,y)
def ternaryToNum2(N,y):
    if N == '':
        return 0
  # if the last digit is a '2'
    elif N[-1] == '2':
        y += 1
        return  ternaryToNum2(N[0:-1],y)+(math.pow(3,y)*2)
    elif N[-1]=='1':
        y+=1
        return ternaryToNum2(N[0:-1],y)+math.pow(3,y)
    else: # last digit must be '0'
        y += 1
        return  ternaryToNum2(N[0:-1],y)


def balancedTernaryToNum(N):
    y=-1
    return balancedTernaryToNum2(N,y)
def balancedTernaryToNum2(N,y):
    if N =='':
        return 0
    elif N[-1]=='+':
        y+=1
        return balancedTernaryToNum2(N[0:-1],y)+math.pow(3,y)
    elif N[-1]=='0':
        y+=1
        return balancedTernaryToNum2(N[0:-1],y)
    else:
        y+=1
        return balancedTernaryToNum2(N[0:-1],y)-math.pow(3,y)
print balancedTernaryToNum('+---0'),'should be 42.0'
print balancedTernaryToNum('++-0+'),'should be 100.0'

def numToBalancedTernary(N):
    if N==0: #code for numToTernary
        return ''
    elif N%3==2:
        return numToBalancedTernary((N+1)/3) +'-'
    elif N%3==1:
        return numToBalancedTernary(N/3) +'+'
    elif N%3==0:
        return numToBalancedTernary(N/3)+'0'
print numToBalancedTernary(42),'should be +---0'
