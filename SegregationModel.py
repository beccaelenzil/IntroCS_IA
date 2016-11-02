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

def populateBoard(width, height, percX, percO):

    A = createBoard(width, height)
    numberofXcells = int((width)*(height)*percX)
    numberofOcells = int((width)*(height)*percO)
    numberofemptycells = (width)*(height) - numberofXcells - numberofOcells
    pop = numberofXcells*['X'] + numberofOcells* ['O'] + numberofemptycells*[" "]
    pop = random.sample(pop, len(pop))
    i = 0
    for row in range(height):
        for col in range(width):
            A[row][col] = pop[i]
            i+=1
    return A


#A = populateBoard(5, 5, 0.4, 0.4)
#printBoard(A)

def countNeighbors(row, col, A):
    counterX = 0
    counterO = 0
    if A[row][col] == 'X' :
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if A[r][c] == 'X':
                    counterX += 1
        if A[row][col] == 'X':
            counterX = counterX - 1
        return counterX
    if A[row][col] == 'O' :
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if A[r][c] == 'O':
                    counterO += 1
        if A[row][col] == 'O':
            counterO = counterO - 1
        return counterO
    if A[row][col] == ' ':
        return ""

A = populateBoard(5,5, 0.4, 0.4)
printBoard(A)
print countNeighbors(1,1,A)
