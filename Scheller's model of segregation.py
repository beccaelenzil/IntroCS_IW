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
    var3=(w*h)-(var1-var2)
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
        return 0

    if countB==0:
        return countA
    else:
        count=countA/(countA+countB)
        return count

def next_life_generation(A):
    """ makes a copy of A and then advances one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays at 0.
    """
# cheak the old model to update the new model
    newA=copy(A)
    h=len(A)
    w=len(A[0])
    for r in range(1,len(A)-1):
        for c in range(1,len(A[0])-1):
            if countNeighbors(r,c,A)<2:
                newA[r][c]=0
            elif countNeighbors(r,c,A)>3:
                newA[r][c]=0
            elif countNeighbors(r,c,A)==3:
                newA[r][c]=1
            else:
                newA[r][c]=A[r][c]
        for row in range (h):
            for col in range (w):
                newA[0][col]=0
                newA[h-1][col]=0
                newA[row][0]=0
                newA[row][w-1]=0
    return newA

A=randomCells(.4,.3,10,10)
printBoard(A)
print countNeighbors(1,1,A)
'''
print ''
for i in range(10):
    A=next_life_generation(A)
    printBoard(A)
    print " "
'''
