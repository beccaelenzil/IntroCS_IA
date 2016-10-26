# python 2
#
# Game of Life
#
# Name: Isabel, Alison
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

#print createBoard(2,2)

def printBoard(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print line

#A = createBoard(5, 3)
#print printBoard(A)

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

#A = diagonalize(3,5)
#print printBoard(A)

def innerCells(width, height):
    A = createBoard(width, height)
    for row in range(1, height-1):
        for col in range(1, width-1):
            A[row][col] = 1
    return A


#A = innerCells(5,5)
#printBoard(A)

def randomCells(width, height):
    A = createBoard(width, height)
    for row in range(1, height-1):
        for col in range(1, width-1):
            A[row][col] = random.choice([0,1])
    return A

#A = randomCells(5,5)
#printBoard(A)
#print

def copy(A):
    height = len(A)
    width = len(A[0])
    newA = randomCells(width, height)
    for row in range(height):
        for col in range(width):
            newA[row][col] = A[row][col]
    return newA

#newA = copy(A)
#printBoard(newA)

def innerReverse(A):
    height = len(A)
    width = len(A[0])
    newA = randomCells(width, height)
    for row in range(1, height-1):
        for col in range(1, width-1):
            if A[row][col] == 1:
                newA[row][col] = 0
            else:
                newA[row][col] = 1
    return newA

#newA = innerReverse(A)
#printBoard(newA)

def countNeighbors(row, col, A):
    counter = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if A[r][c] == 1:
                counter = counter + 1
    if A[row][col] == 1:
        counter = counter - 1
    return counter

#A = randomCells(5,5)
#printBoard(A)
#print countNeighbors(1,1,A)


def next_life_generation(A):
    """ makes a copy of A and then advances one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays at 0.
    """
    newA = copy(A)
    height = len(A)
    width = len(A[0])
    for row in range(1, width-1):
        for col in range(1, height-1):
            if countNeighbors(row, col, A) < 2:
                newA[row][col] = 0
            if countNeighbors(row, col, A) > 3:
                newA[row][col] = 0
            if countNeighbors(row, col, A) == 3:
                newA[row][col] = 1
    return newA

A = randomCells(5,5)
newA = next_life_generation(A)
printBoard(A)
print " "
printBoard(newA)
