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

def innerCells1(width, height):
    A = createBoard(width, height)
    printBoard(A)
    for row in range(height):
        for col in range(width):
            if row == 0:
                A[row][col] = 0
            elif row == width-1:
                A[row][col] = 0
            elif col == 0:
                A[row][col] = 0
            elif col == height-1:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A

def innerCells(width, height):
    A = createBoard(width, height)
    for row in range[1:height-2]:
        for col in range[1:width-2]:
            A[row][col] = 1
    return A


A = innerCells(5,5)
printBoard(A)
