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
    if n==0:
        f=0
    elif n%2==0:
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
def listReverse(L):
    L1=[]
    listReverse2(L, L1)
    return L1

def listReverse2(L, L1):
    if len(L)==0:
        return L1
    else:
        list.append(L1,list.pop(L,-1))
        listReverse2(L, L1)
    return L1


#this is not an iterative solution, it's a slicing one
def listReverseIter(L):
    L1=[]
    for i in range(len(L)):
        x=list.pop(L,-1)
        list.append(L1,x)
    return L1

print "listReverse([1,2,3,4]) == [4,3,2,1] = ",listReverse([1,2,3,4])," : ",listReverse([1,2,3,4]) == [4,3,2,1]
print "listReverseIter([1,2,3,4]) == [4,3,2,1] = ",listReverseIter([1,2,3,4])," : ",listReverseIter([1,2,3,4]) == [4,3,2,1]
