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

    while n > 1:
        result = n + result
        n = n - 1
        return result


print "fibIter(5) == 5 = ",fibIter(5)," : ", 5 == fibIter(5)
print "fibIter(11) == 89 = ",fibIter(11)," : ", 89 == fibIter(11)

