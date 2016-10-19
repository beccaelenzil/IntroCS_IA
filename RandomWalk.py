# python 2
#
# Homework 5, Problem 1
#
# Name: Isabel Alexander
#

import random
import time

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])

def rwpos(start, nsteps):
    """Function that simulates a sleepwalker. The sleepwalker starts at start, an integer representing
    the starting location. For nsteps number of steps, the sleepwalker takes a random step either
    forwards or backwards.
    """
    currentposition = start
    for i in range(nsteps):
        currentposition = currentposition + rs()
        print "Current position is ", currentposition
    return currentposition

#print rwpos(3, 7)

def rwsteps(start, low, high):
    """Function that simulates a sleepwalker. The sleepwalker begins at start, an integer that represents
    the starting position. Then, the sleepwalker takes random steps either forwards or backwards until
    it reaches either the low value or the high value.
    """
    currentposition = start
    counter = 0
    while currentposition != low and currentposition != high:
        beforespaces = currentposition-low-1
        afterspaces = high-currentposition-1
        #print beforespaces
        #print afterspaces
        print "low|" + " "*(beforespaces) + "s" + " "*(afterspaces) + "|high"
        currentposition = currentposition + rs()
        counter = counter + 1
        time.sleep(0.1)
    return counter

#print rwsteps(5, 0, 10)


def rwposPlain(start, nsteps):
    """Function that simulates a sleepwalker. The sleepwalker starts at start, an integer representing
    the starting location. For nsteps number of steps, the sleepwalker takes a random step either
    forwards or backwards.
    """
    currentposition = start
    for i in range(nsteps):
        currentposition = currentposition + rs()
    return currentposition

#print rwposPlain(10, 20)

def ave_signed_displacement(numtrials):
    """Function that computes the average signed displacement value for the rwposPlain function
    numtrials number of times.
    """
    results = []
    for i in range(numtrials):
        results.append(rwposPlain(0, 100))
    print results
    print sum(results)
    print len(results)
    return float(sum(results))/len(results)

print ave_signed_displacement(4)
print

def ave_squared_displacement(numtrials):
    """Funtion that computes the average squared dispacement value for the rwposPlain function
    numtrials number of times.
    """
    results = []
    resultssquared = []
    for i in range(numtrials):
        results.append(rwposPlain(0, 100))
    for i in results:
        resultssquared.append(i**2)
    print results
    print resultssquared
    print sum(resultssquared)
    print len(resultssquared)
    return float(sum(resultssquared))/len(resultssquared)

#print ave_squared_displacement(4)
