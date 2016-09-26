# python 2
#
# Homework 3, Problem 1
# Loops!
#
# Name: Isabel Alexander
#

def fac(n):
    """ loop-based factorial function
        input: a nonnegative integer n
        output: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

# tests: run by pressing the Run button above

print "fac(0): should be 1 == ", fac(0)
print "fac(5): should be 120 == ", fac(5)

#Problem 1a

def power(b,p):
    """ loop-based power function
        input: a numeric value for the base, b, and any nonnegative interger for the power, p
        output: b to the power of p
    """
    result = 1

    for x in range(p):     # loop from 1 to n, inclusive
        result = result*b    # update the result by mult. by x
    return result              # notice this is AFTER the loop!


print "power(2,5): should be 32 == ", power(2,5)
print "power(5,2): should be 25 == ", power(5,2)
print "power(42,0): should be 1 == ", power(42,0)
print "power(0,42): should be 0 == ", power(0,42)
print "power(0,0): should be 1 == ", power(0,0)
