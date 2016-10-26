# python 2
#
# Homework 5, Problem 1
#
# Name: Isabel Alexander
#

import random
import time
import matplotlib.pyplot as plt

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
    #print results
    #print sum(results)
    #print len(results)
    return float(sum(results))/len(results)

#print ave_signed_displacement(10000)

def ave_squared_displacement(numtrials):
    """Funtion that computes the average squared dispacement value for the rwposPlain function
    numtrials number of times.
    """
    results = []
    resultssquared = []
    for i in range(numtrials):
        results.append(abs(rwposPlain(0, 100)))
    for i in results:
        resultssquared.append(i**2)
    #print results
    #print resultssquared
    #print sum(resultssquared)
    #print len(resultssquared)
    #print results
    #print " "
    #print resultssquared
    return [float(sum(resultssquared))/len(resultssquared), results, resultssquared]


[ave, results, resultssquared] = ave_squared_displacement(10000)

plt.figure(0)
plt.hist(results)
plt.title("pos")


plt.figure(1)
plt.hist(resultssquared)
plt.title("pos sq")


'''
1) What is the average final signed-displacement for a random walker after
making 100 random steps? What about after N random steps? As described above,
the signed-displacement is just the output of rwpos minus the start location. Do not use abs.

The average signed-displacement for a random walker after making 100 random steps
is 0. This makes sense logically because for every step, the random walker has a 50% chance
of walking forwards and a 50% chance of walking backwards. So, as the walker takes more and more
steps, you would expect the walker to end up very close to where it started. This is what my
average signed-displacement function showed, for example after running the function three times
with 10000 trials, it returned average signed-displacement values of 0.0466, -0.011, and 0.0032.
This logic holds true for N number of steps as well. The average final signed-displacement
value would still be 0, although this value will become increasingly accurate with increasing
numbers of trials. I approached this question by thinking logically about probabilities.
I guessed that the values would be close to zero, and then confirmed with my function.

2) What is the average squared-displacement for a random walker after making
 100 random steps? What about after N random steps, in terms of N? Be sure you
 square the signed displacements before you sum the values in order to average them!

The average squared-displacement for a random walker after making 100 random steps is 100.
After N random steps, the average squared-displacement is N. My function returned values
of 100.9328, 100.11, and 99.5768 when the function averaged the square of 10000 trials. This
makes sense because in this case, the function assumed the sleep walker was taking 100 steps.
This question was harder for me to think about in terms of probabilities, so instead I used
my function to test out different values. I found that the number of random steps taken was
always close to the value that the function returned.

'''
