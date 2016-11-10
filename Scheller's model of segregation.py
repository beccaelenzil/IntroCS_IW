import random

def createOneRow(width): #create row
    row = []
    for col in range(width):
        row += [0]
    return row
def createBoard(width, height): #returns a 2d array with "height" rows and "width" cols
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A
def printBoard(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print line

    return A

def randomCells(percentofA,percentofB,w, h):
    var1=percentofA*(w*h)
    var2=percentofB*(w*h)
    var1=int(var1)
    var2=int(var2)
    numassign=0
    var3=(w*h)-var1-var2
    assignlist=var1*['A']+var2*['B']+var3*[' ']
    assignlist1=random.sample(assignlist,len(assignlist))
    A = createBoard(w, h)
    for row in range (0,h):
        for col in range (0,w):
            A[row][col]=assignlist1[numassign]
            numassign+=1
    return A

def copy(A):
    h=len(A)
    w=len(A[0])
    newA=createBoard(h,w)
    for row in range (h):
        for col in range (w):
            newA[row][col]=A[row][col]
    return newA

def innerReverse(A):
    h=len(A)
    w=len(A[0])
    newA=copy(A)
    for row in range (h):
        for col in range (w):
            newA[0][col]=1
            newA[h-1][col]=1
            newA[row][0]=1
            newA[row][w-1]=1
#reverse, it works
    for row in range(0,h):
        for col in range(0,w):
            if newA[row][col]==1:
                newA[row][col]=0
            else:
               newA[row][col]=1
    return newA

def countNeighbors(row,col,A):
    countA=-1
    countB=0
    if A[row][col]=='A':
        for r in range(row-1,row+2):
            for c in range(col-1,col+2):
                if A[r][c]=='A':
                    countA+=1.0
                elif A[r][c]=='B':
                    countB+=1.0
    elif A[row][col]=='B':
        for r in range(row-1,row+2):
            for c in range(col-1,col+2):
                if A[r][c]=='B':
                    countA+=1.0
                elif A[r][c]=='A':
                    countB+=1.0
    elif A[row][col]==' ':
        return -1

    if countB==0:
        return countA
    else:
        count=countA/(countA+countB)
        return count
def emptylist(A):
    emptylist1=[]
    for r in range(0,len(A)-1):
        for c in range(0,len(A[0])-1):
            if A[r][c]==' ':
                emptylist1.append([r,c])
            else:
                pass
    return emptylist1

def emptycells(emptylist,row,col,A):
    z=0
    h=len(A)
    w=len(A[0])
    rdif=1
    cdif=1
    while z==0:
        for r in range(row-rdif,row+(rdif+1)):
            for c in range(col-cdif,col+(cdif+1)):
                try:
                    for x in range(len(emptylist)):
                        if A[r][c]==' 'and r==emptylist[x][0]and c==emptylist[x][1]:
                            list.pop(emptylist,x)
                            cord=[r,c,emptylist]
                            z=1
                            return cord
                except:
                    pass
        rdif+=1
        cdif+=1
        if rdif>=h and cdif>=w:
            z=1
            return -1

def next_life_generation(A,T):
    emptylist1=emptylist(A)
    newA=copy(A)
    h=len(A)
    w=len(A[0])
    for r in range(0,len(A)-1):
        for c in range(0,len(A[0])-1):
            #below percent stays the same, also does spaces
            if countNeighbors(r,c,A)>=T:
                newA[r][c]=A[r][c]
            elif countNeighbors(r,c,A)<T and A[r][c] != -1:
                cord=emptycells(emptylist1,r,c,A)
                if cord==-1:
                    pass
                else:
                    newA[r][c]=' '
                    newA[cord[0]][cord[1]]=A[r][c]
                    emptylist1=cord[2]
    return newA

A=randomCells(.3,.3,5,5)
printBoard(A)
print '------------------'
B=next_life_generation(A,.5)
printBoard(B)
print '------------------'
C=next_life_generation(A,.5)
printBoard(C)
