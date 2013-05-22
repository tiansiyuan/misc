#!/usr/bin/env python

import math

MAX = 10000 # upper limit
primes = []
ndiv = {}

def isPrime(x):
    if x in primes: return x
    for i in primes:
        if not x % i: return None
    else:
        primes.append(x)
        return x

filter(isPrime, range(2, MAX))


for p in primes:
    for n in xrange(2, p-1):
        nfac = math.factorial(n)
        if n not in ndiv.keys():
            ndiv[n] = reduce(lambda x,y: x+nfac/y, xrange(2,n+1), nfac)
        
        if ndiv[n] % p == 0:
            print "p = %d, n = %d" % (p, n)
            break
