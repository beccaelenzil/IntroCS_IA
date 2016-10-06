#rectangle

def printRect(width, height, symbol):

    """loop-based function that creates a rectangle with dimensions width x height using a symbol entered.
        input: two positive integers width and height and a symbol that will be used for the rectangle
        output: a rectangle made up of a symbol with dimensions width x height
    """
    for x in range(height):
        print symbol*width


printRect( 4, 6, '%' )
printRect( 2, 1, '$' )
printRect( 5, 0, '#' )
printRect( 0, 8, '@' )
printRect( 7, 9, '#')

#Triangle

def printTriangle(width, symbol, rightsideup):

    counter = 1

    if counter < width:
        print symbol*counter
        counter = counter + 1

printTriangle( 3, '@', True )
