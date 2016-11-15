from SchellersModel import *
from visual import *

def constants():
    width = 40
    height = 40
    cell_size = 15
    spacing = 1
    return [width,height,cell_size,spacing]

def drawBoard(A):
    [width,height,cell_size,spacing] = constants()
    for row in range(height):
        x_pos = spacing+row*(cell_size+spacing)
        for col in range(width):
            y_pos = spacing+col*(cell_size+spacing)
            if A[row][col] == 'A':
                box(pos=(x_pos,y_pos,0), size=(cell_size,cell_size,0), color=color.blue)
            elif A[row][col] == 'B':
                box(pos=(x_pos,y_pos,0), size=(cell_size,cell_size,0), color=color.magenta)
            elif A[row][col] == ' ':
                box(pos=(x_pos,y_pos,0), size=(cell_size,cell_size,0), color=color.white)


[w,h,cell_size,spacing] = constants()

w_window = w*(cell_size+spacing)
h_window = h*(cell_size+spacing)

gameOfLifeWindow = display(title='Schellers\'s Model of Segregation',
     x=0, y=0, width=w_window, height=h_window,
     center=(w_window/2,h_window/2,0), background=(1,1,1))

gameOfLifeWindow.exit = True

A = randomCells(.4,.4,40,40)
drawBoard(A)

while True:
    A = next_life_generation(A,5)
    print A
    drawBoard(A)
    rate(30)
