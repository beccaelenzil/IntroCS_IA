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
    for row in range(1, height-1):
        for col in range(1, width-1):
            A[row][col] = pop[i]
            i+=1
    return A


#A = populateBoard(5, 5, 0.4, 0.4)
#printBoard(A)

def countNeighbors(A):
    height = len(A)
    width = len(A[0])
    counterX = 0
    counterO = 0
    counterTotal = 0
    ratio = 0
    ratioBoard = createBoard(width, height)

    for row in range(1, height-1):
        for col in range(1, width-1):
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if A[r][c] == 'X':
                        counterX += 1
                    elif A[r][c] == 'O':
                        counterO += 1
            counterTotal = counterO + counterX - 1
            if A[row][col] == 'X':
                counterX = counterX - 1
                ratio = float(counterX)/counterTotal
            elif A[row][col] == 'O':
                counterO == counterO - 1
                ratio = float(counterO)/counterTotal
            else:
                ratio = None
            #return ratio
            ratioBoard[row][col] = ratio
    return ratioBoard

def index(A):
    height = len(A)
    width = len(A[0])
    emptylist = []
    for row in range(1, height-1):
        for col in range(1, width-1):
            if A[row][col] == " ":
                emptylist.append([row, col])
    return emptylist


def SegregationModel(A, threshold, percX, percO):
    height = len(A)
    width = len(A[0])
    i = 0
    newA = populateBoard(width, height, percX, percO)
    ratioBoard = countNeighbors(A)
    emptylist = index(A)
    for row in range(1, height-1):
        for col in range(1, width-1):
            if A[row][col] < threshold:
                newA[row][col] = " "
                [er, ec] = [emptylist[i][0], emptylist[i][1]]
                if A[row][col] == 'X':
                    newA[er][ec] = 'X'
                if A[row][col] == 'O':
                    newA[er][ec] = 'O'
                i += 1
            elif A[row][col] > threshold:
                newA[row][col] = A[row][col]
    return newA


A = populateBoard(5,5, 0.4, 0.4)
printBoard(A)
print
printBoard(countNeighbors(A))
print index(A)
newA = SegregationModel(A, .4, .4, .4)
printBoard(newA)
