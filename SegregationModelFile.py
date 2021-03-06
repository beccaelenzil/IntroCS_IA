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

def copy(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            newA[row][col] = A[row][col]
    return newA


def printBoard(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print line

def populateBoard(width, height, percX, percO):

    A = createBoard(width, height)
    numberofXcells = int((width-2)*(height-2)*percX)
    numberofOcells = int((width-2)*(height-2)*percO)
    numberofemptycells = int(width-2)*(height-2) - numberofXcells - numberofOcells
    #print "number of empty:" , numberofemptycells
    #print "number of X:", numberofXcells
    #print "number of O:", numberofOcells
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

    ratioBoard = createBoard(width, height)
    OBoard = createBoard(width, height)
    XBoard = createBoard(width, height)
    counterTotalBoard = createBoard(width, height)
    #counterOBoard = createBoard(width, height)

    for row in range(1, height-1):
        for col in range(1, width-1):
            counterX = 0
            counterO = 0
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if A[r][c] == 'X':
                        counterX += 1
                    elif A[r][c] == 'O':
                        counterO += 1

            counterTotal = counterO + counterX - 1

<<<<<<< Updated upstream:SegregationModelFile.py
            if A[row][col] == 'O' and counterTotal != 0:
<<<<<<< HEAD
                counterO == counterO - 1
=======
            if A[row][col] == 'X' and counterTotal != 0:
                counterX = counterX - 1
                ratio = float(counterX)/counterTotal
            elif A[row][col] == 'O' and counterTotal != 0:
                counterO = counterO - 1
>>>>>>> Stashed changes:SegregationModel.py
=======
                counterO = counterO - 1
>>>>>>> origin/master
                ratio = float(counterO)/counterTotal
            elif A[row][col] == 'X' and counterTotal != 0:
                counterX = counterX - 1
                ratio = float(counterX)/counterTotal
            else:
                ratio = None



            ratioBoard[row][col] = ratio
            OBoard[row][col] = counterO
            XBoard[row][col] = counterX
            counterTotalBoard[row][col] = counterTotal
<<<<<<< HEAD
<<<<<<< Updated upstream:SegregationModelFile.py
            counterOBoard[row][col] = counterX

    return counterOBoard
=======

    return [ratioBoard, OBoard, XBoard, counterTotalBoard]
>>>>>>> Stashed changes:SegregationModel.py
=======
            #counterOBoard[row][col] = counterO

    return ratioBoard
>>>>>>> origin/master

def index(A):
    height = len(A)
    width = len(A[0])
    emptylist = []
    for row in range(1, height-1):
        for col in range(1, width-1):
            if A[row][col] == " ":
                emptylist.append([row, col])
    random.shuffle(emptylist)
    return emptylist


def SegregationModel(A, threshold, percX, percO):
    height = len(A)
    width = len(A[0])
    newA = copy(A)
    i = 0
    ratioBoard = countNeighbors(A)
    emptylist = index(A)
    for row in range(1, height-1):
        for col in range(1, width-1):
            if ratioBoard[row][col] < threshold and i < len(emptylist) and ratioBoard[row][col] != None:
                newA[row][col] = " "
                [er, ec] = [emptylist[i][0], emptylist[i][1]]
                #print 'row,col: ',[row,col]
                #print 'er,ec: ',[er, ec]
                newA[er][ec] = A[row][col]
                i += 1
                #print len(emptylist), i
    return newA


A = populateBoard(10, 10, 0.4, 0.4)
printBoard(A)
<<<<<<< Updated upstream:SegregationModelFile.py
ratioBoard = countNeighbors(A)
print " "
#printBoard(ratioBoard)
print
#printBoard(ratioBoard)
#print
#print index(A)
newA = SegregationModel(A, .4, .4, .4)

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

print
print segregationIndex(newA)

#print
#print segregationIndex(newA)

=======
print " "
[ratioBoard, OBoard, XBoard,counterTotalBoard] = countNeighbors(A)
printBoard(OBoard)
print " "
printBoard(XBoard)
print " "
printBoard(counterTotalBoard)
'''
#print
#print index(A)
newA = SegregationModel(A, .4, .4, .4)
printBoard(newA)
'''
>>>>>>> Stashed changes:SegregationModel.py
