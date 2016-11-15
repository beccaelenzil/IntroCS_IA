from SegregationModelFile import *
from visual import *

def constants():
    width = 40
    height = 40
    cell_size = 18
    spacing = 2
    return [width,height,cell_size,spacing]

def drawBoard(A):
    [width,height,cell_size,spacing] = constants()
    for row in range(height):
        x_pos = (cell_size + spacing)*(row)
        for col in range(width):
            y_pos = (cell_size + spacing)*(col)
            if A[row][col] == 'X':
                box(pos=(x_pos,y_pos,0), size=(cell_size,cell_size,0), color=color.red)
            elif A[row][col] == 'O':
                box(pos=(x_pos,y_pos,0), size=(cell_size,cell_size,0), color=color.blue)
            elif A[row][col] == ' ':
                box(pos=(x_pos,y_pos,0), size=(cell_size, cell_size,0), color=color.white)


[w, h, cell_size, spacing] = constants()

w_window = w*(cell_size+spacing)
h_window = h*(cell_size+spacing)

SegregationModelSim = display(title='Segregation Model',
     x=0, y=0, width=w_window, height=h_window,
     center=(w_window/2,h_window/2,0), background=(1,1,1))

SegregationModel.exit = True

A = populateBoard(w, h, .4, .4)
drawBoard(A)

def segregationIndex(A):
    ratioBoard = countNeighbors(A)
    segregationList = []
    height = len(A)
    width = len(A[0])
    for row in range(height):
        for col in range(width):
            if A[row][col] != ' ':
                segregationList.append(ratioBoard[row][col])
            else:
                segregationList = segregationList


    segregationIndex = sum(segregationList)/len(segregationList)

    return segregationIndex


'''
while True:
    A = SegregationModel(A, .5, .4, .4)
    drawBoard(A)
    rate(30)
'''

newA = SegregationModel(A, .4, .4, .4)
printBoard(countNeighbors(newA))

