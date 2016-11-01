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

def populateBoard(A):
    height = len(A)
    width = len(A[0])
    counterX = 0
    counterO = 0
    counterempty = 0
    numberofXcells = (width)*(height)*(1/3)
    numberofOcells = (width)*(height)*(1/3)
    numberofemptycells = (width)*(height) - numberofXcells - numberofOcells
    for row in range(height):
        for col in range(width):
            while counterX <= numberofXcells:
                while counterO <= numberofOcells:
                    while counterempty <= numberofemptycells:
                        A[row][col] = random.choice['X', 'O', " "]
                        if A[row][col] == 'X':
                            counterX += 1
                        elif A[row][col] == 'O':
                            counterO += 1
                        else:
                            counterempty += 1

