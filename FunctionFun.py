import math

#Example Problem
def tpl(x):
    """  output: tpl returns three times its input
         input x: a number (int or float)
         Spam is great, and tpl("spam") is better!
    """
    return 3*x

#Problem 1

def sq(x):
    """"" output: sq returns the imput squared
        imput x: a number (int or float)
    """

    return x*x

#Problem 2

def interp(low, high, fraction):
    """ output: interp returns a value that is a fraction of the way from the first number to the second numer
        imput: 3 numbers (low, high, fraction)
    """
    return ((high - low)*fraction) + low

print interp(1.0, 9.0, .25)
print interp(24, 42, 0)
print interp(102, 117, -4.0)

#Problem 3

def checkends(s):
    """" output: If the first and last characters in the string are the same, checkends returns True.
    If they do not match, the function returns False.
        imput: a string
    """
    if s[0] == s[-1] :
        return True
    else:
        return False

print checkends('no match')
print checkends('hah! a match')
print checkends('q')
print checkends(' ')

#Problem 4

def flipside(s):
    """" output: flipside takes a string (s) and returns a string whose first half is s's second half
                and second half is s's first half. If the string (s) has an odd number of characters,
                the first half of the imput string should have one fewer letters than the second half.
                Conversely, the second half of the output should have one fewer letters than the first half.
        imput: a string
    """
    remainder = len(s)%2
    if remainder == 0:
        return s[len(s)/2:] + s[:len(s)/2]

    else:
        return s[len(s)/2:] + s[:len(s)/2]

print flipside('homework')
print flipside('carpets')

#Problem 5

def convertFromSeconds(s):
    """ output: a list, L, of four nonnegative integers that represents s in traditional units of time.
        The first element is the number of days, the second is the number of hours,
        the third is the number of minutes, and the fourth is the number of seconds.
        imput: s, a nonnegative integer number of seconds
    """
    days = s / (24*60*60)  # # of days
    s = s % (24*60*60)     # the leftover
    hours = s / (60*60)
    s = s % (60*60)
    minutes = s / 60
    seconds = s % 60
    return [days, hours, minutes, seconds]

print convertFromSeconds(200000)

#Problem 6

def front3(str):

    """ output: front3 returns a new string that is the first three characters of the imput string repeated
    three tiems. If the imput string is less than three characters long, the function returns the entire string
    repeated three times.
    imput: a string
    """
    return 3*str[:3]


print front3('string')
print front3('Ha')
