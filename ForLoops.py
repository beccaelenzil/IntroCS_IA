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

#Problem 1c

def mult(n,m):
    """loop-based function that multiplies two numbers together
        input: two integers, m and n
        output: the product of m times n
    """
    result = 0

    if m == 0 or n == 0:
        result = 0

    elif n > 0:
        for x in range(n):
            result = result + m
    else:
        for x in range(-n):
            result = result - m
    return result

# Tests

print "mult(6,7)    42 ==", mult(6,7)
print "mult(6,-7)  -42 ==", mult(6,-7)
print "mult(-6,7)  -42 ==", mult(-6,7)
print "mult(-6,-7)  42 ==", mult(-6,-7)
print "mult(6,0)     0 ==", mult(6,0)
print "mult(0,7)     0 ==", mult(0,7)
print "mult(0,0)     0 ==", mult(0,0)


#Problem 1d

def dot(L,K):
    """ Loop-based function that finds the dot product of the lists L and K
        input: Two lists with numeric values, L and K
        output: the dot product of lists L and K
    """
    result = 0

    if len(L) != len(K):
        result = 0
    else:
        for x in range(len(L)):
            result = result + (L[x]*K[x])

    return result

# Tests
#

print "dot( [5,3], [6,4] )     42.0 ==", dot( [5,3], [6,4])
print "dot( [1,2,3,4], [10,100,1000,10000] )  43210.0 ==", dot( [1,2,3,4], [10,100,1000,10000] )
print "dot( [5,3], [6] )        0.0 ==", dot( [5,3], [6] )
print "dot( [], [6] )           0.0 ==", dot( [], [6] )
print "dot( [], [] )            0.0 ==", dot( [], [] )

#Problem 1e

def count_evens(L):
    """loop-based function that counts the number of even integers in a given array
    input: an array L (a list?)
    output: an integer that represents the number of even integers in the array
    """
    result = 0
    for x in L:
        if x%2 == 0:
            result = result + 1
    return result

print "count_evens([2, 1, 2, 3, 4], 3 == ", count_evens([2, 1, 2, 3, 4])
print "count_evens([2, 2, 0]), 2 == ", count_evens([2, 2, 0])
print "count_evens([1, 3, 5]), 0 == ", count_evens([1, 3, 5])


#Problem 1f

def count9(L):
    """loop-based function that counts the number of 9s in a given array
        input: an array L (a list?)
        output: an integer representing the number of 9s in a given array
    """
    result = 0
    for x in L:
        if x == 9:
            result = result + 1
    return result

# Tests

print "count9([1, 2, 9]), 1 == ",count9([1, 2, 9])
print "count9([1, 9, 9]), 2 == ",count9([1, 9, 9])
print "count9([1, 9, 9, 3, 9]), 3 == ",count9([1, 9, 9, 3, 9])

