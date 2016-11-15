
import pygame
from GameOfLife import *
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
            if A[row][col] == 1:
                box(pos=(x_pos,y_pos,0), size=(cell_size,cell_size,0), color=color.white)
            elif A[row][col] == 0:
                box(pos=(x_pos,y_pos,0), size=(cell_size,cell_size,0), color=color.black)


[w,h,cell_size,spacing] = constants()

w_window = w*(cell_size+spacing)
h_window = h*(cell_size+spacing)

gameOfLifeWindow = display(title='Game Of Life',
     x=0, y=0, width=w_window, height=h_window,
     center=(w_window/2,h_window/2,0), background=(1,1,1))

gameOfLifeWindow.exit = True

A = randomCells(w,h)
drawBoard(A)

while True:
    A = next_life_generation(A)
    drawBoard(A)
    rate(30)



'''

screen_width = 500
screen_height = 500

pygame.init()

# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("PyGame Check")

# Loop until the user clicks the close button.
done = False

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
'''
