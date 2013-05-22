#!/usr/bin/env python                                                                                                                 
MAX = 10000 # upper limit                                                                                                            
primes = []

def isPrime(x):
    if x in primes: return x
    for i in primes:
        if not x % i: return None
    else:
        primes.append(x)
        return x

def findsprime(x):
    while x not in sprimes:
        x -= 1
    return sprimes.index(x)

with open("./sprimes.txt") as f:
    numbers = f.readlines()
    sprimes = eval(str(numbers[0]))

statis = {}

for i in xrange(100, MAX+1, 100):
    if i == 100:
        filter(isPrime, range(2, i))
    else:
        filter(isPrime, range(i-100+1, i))
    
    sindex = findsprime(i)

    statis[i] = (len(primes), primes[-1], sindex+1) 

for key in sorted(statis.iterkeys()):
    (noOfPrimes, maxPrime, sindex) = statis[key]
    print key, 1.0*sindex/noOfPrimes
