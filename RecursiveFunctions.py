#https://beccaelenzil_gmail_com.trinket.io/introduction-to-computer-science#/recursion/problem-4-1-recursive-drawing
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibIter(n):
    f0=0
    f1=1
    if n%2==0:
        for x in range(n/2):
            f1+=f0
            f0+=f1
            f=f0
    else:
        for x in range((n/2)+1):
            f1+=f0
            f0+=f1
            f=f1
    return f

print "fib(5) == 5 = ",fib(5)," : ", 5 == fib(5)
print "fib(11) == 89 = ",fib(11)," : ", 89 == fib(11)
print "fibIter(5) == 5 = ",fibIter(5)," : ", 5 == fibIter(5)
print "fibIter(11) == 89 = ",fibIter(11)," : ", 89 == fibIter(11)
invl=[]
def listReverse(L):
    if len(L)==0:
        return invl
    else:
        list.append(invl,L[-1])
        L=L[0:-1]
        listReverse(L)
    return invl

def listReverseIter(L):
    return L[-1::-1]

print "listReverse([1,2,3,4]) == [4,3,2,1] = ",listReverse([1,2,3,4])," : ",listReverse([1,2,3,4]) == [4,3,2,1]
print "listReverseIter([1,2,3,4]) == [4,3,2,1] = ",listReverseIter([1,2,3,4])," : ",listReverseIter([1,2,3,4]) == [4,3,2,1]
