import random

def createOneRow(width): #create row
    row = []
    for col in range(width):
        row += [' ']
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
    newA=createBoard(w,h)
    for row in range(h-1):
        for col in range(w-1):
            newA[row][col]=A[row][col]
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

def next_life_generation_simple(A,T):
    emptylist1=emptylist(A)
    random.shuffle(A)
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
                if emptylist1==[]:
                    pass
                else:
                    newA[r][c]=' '
                    newA[emptylist1[0][0]][emptylist1[0][1]]=A[r][c]
                    list.pop(emptylist1,0)
#stoping point!!!! static check
    if newA == A:

        static = (newA == A)
        return [static, A]
    else:
        return newA

def segregationIndex(A):
    """
    takes in a matrix and returns a segregation index
    """
    height=len(A)
    width=len(A[0])
    segregation = copy(A)
    segregationList = []

    for row in range(0,height-1):
        for col in range(0,width-1):
            if A[row][col] != ' ':
                segregation[row][col] = countNeighbors(row,col,A)
                # I could make a heat map of segregation

                # put it into a list so we can easily take the average
                segregationList.append(segregation[row][col])

    # take the average of the segregationIndex for each cell to get a single metric
    segregationIndex = sum(segregationList)/len(segregationList)

    return [segregation, segregationIndex]
'''
A=randomCells(.3,.3,15,15)
printBoard(A)
print segregationIndex(A)[1]
print '------------------'
B=next_life_generation(A,.5)
printBoard(B)
print segregationIndex(B)[1]
print '------------------'
C=next_life_generation(A,.5)
printBoard(C)
print segregationIndex(C)[1]
'''

count=0
A=randomCells(.3,.3,15,15)
printBoard(A)
print segregationIndex(A)[1]
count=0
print '------------------'
B=next_life_generation_simple(A,.5)
printBoard(B)
print segregationIndex(B)[1]
print '------------------'
C=next_life_generation_simple(A,.5)
printBoard(C)
print segregationIndex(C)[1]

