#!/usr/bin/env python                                                                                                                 
MAX = 30000 # upper limit
STEP = 1000                                                                                                            
primes = []
statis = {}

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

for i in xrange(STEP, MAX+1, STEP):
    if i == STEP:
        filter(isPrime, range(2, i))
    else:
        filter(isPrime, range(i-STEP+1, i))

    statis[i] = len(primes)

with open("./sp30k2.txt") as f:
    numbers = f.readlines()

num = 0.0
for key in sorted(statis.iterkeys()):
    num += int(numbers[key/STEP-1])
    print key, num/statis[key]
