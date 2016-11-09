# python 2
#
# Game of Life
#
# Name:
#

import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row
def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
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
def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A
def innerCells(w, h):
    A = createBoard(w, h)
    for row in range (1,h-1):
        for col in range (1,w-1):
            A[row][col]=1
    return A

def randomCells(w, h):
    A = createBoard(w, h)
    for row in range (1,h-1):
        for col in range (1,w-1):
            A[row][col]=random.randint(0,1)
    return A

def copy(A):
    h=len(A)
    w=len(A[0])
    newA=createBoard(w,h)
    for row in range(h):
        for col in range(w):
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
    count=0
    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            count+=A[r][c]
    count-=A[row][col]
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

A=randomCells(10,10)
printBoard(A)
print ''
for i in range(10):
    A=next_life_generation(A)
    printBoard(A)
    print " "

