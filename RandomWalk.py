# python 2
#
# Homework 5, Problem 1
#
# Name: Isabel Alexander
#

import random

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])

def rwpos(start, nsteps):
    currentposition = start
    for i in range(nsteps):
        currentposition = currentposition + rs()
        print "Current position is ", currentposition

print rwpos(3, 7)
