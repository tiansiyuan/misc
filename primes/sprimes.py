#!/usr/bin/env python

import math

max = 10000 # upper limit
primes = []

def isPrime(x):
    if x in primes: return x
    for i in primes:
        if not x % i: return None
    else:
        primes.append(x)
        return x

filter(isPrime, range(2,max))


for p in primes:
    for n in xrange(2, p-1):
        nfac = math.factorial(n)
        ndiv = 0
        for i in xrange(1,n+1):
            ndiv += nfac/i

        if ndiv % p == 0:
            print "p = %d, n = %d" % (p, n)
            break
