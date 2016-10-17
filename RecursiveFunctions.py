#https://trinket.io/python/85ef3ed403


def fib(n):
    """Function that returns the nth term of the Fibonnaci sequence. The Fibonnaci sequence
        is found by adding the previous two terms.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib (n-2)


print "fib(5) == 5 = ",fib(5)," : ", 5 == fib(5)
print "fib(11) == 89 = ",fib(11)," : ", 89 == fib(11)

def fibIter(n):
    """"Function that returns the nth term of the Fibonnaci sequence. The Fibonnaci sequence
    is found by adding the previous two terms.
    """
    result = [0,1]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for x in range(2, n+1):
            result.append(result[x-1] + result[x-2])
        return result[-1]


print "fibIter(5) == 5 = ",fibIter(5)," : ", 5 == fibIter(5)
print "fibIter(11) == 89 = ",fibIter(11)," : ", 89 == fibIter(11)


def listReverse(L):
    """Recursive function that takes in a list L as an argument and returns the list L in reverse order.
    """

    if len(L) == 1:
        return L
    else:
        return listReverse(L[1:]) + [L[0]]

def listReverseIter(L):
    """Iterative function that takes in a list L as an argument and returns the list L in reverse order.
    """
    length = len(L)
    reverselist = []

    for i in L:
        reverselist.append(L[length-1])
        length = length - 1

        if length == 0:
            return reverselist


# List Reverse Tests
print "listReverse([1,2,3,4]) == [4,3,2,1] = ",listReverse([1,2,3,4])," : ",listReverse([1,2,3,4]) == [4,3,2,1]
print "listReverseIter([1,2,3,4]) == [4,3,2,1] = ",listReverseIter([1,2,3,4])," : ",listReverseIter([1,2,3,4]) == [4,3,2,1]



