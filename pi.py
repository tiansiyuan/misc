#!/usr/bin/env python

# three formula to calculate pi


# Bailey-Borwein-Plouffe formula
# Bellard's formula
# Chudnovsky algorithm

import sys
import math
from decimal import *

def main1(argv):
    if len(argv) != 1:
        sys.exit('Usage: pi.py <n>')

    print '\nComputing Pi v.01\n'

    a = Decimal(1.0)
    b = Decimal(1.0)/Decimal(math.sqrt(2))
    t = Decimal(1.0)/Decimal(4.0)
    p = Decimal(1.0)

    for i in range(int(sys.argv[1])):
        at = Decimal((a+b)/2)
        bt = Decimal(math.sqrt(a*b))
        tt = Decimal(t - p*(a-at)**2)
        pt = Decimal(2*p)
         
        a = at;b = bt;t = tt;p = pt

    my_pi = (a+b)**2/(4*t)
    accuracy = 100*(Decimal(math.pi)-my_pi)/my_pi

    print "Pi is approximately: " + str(my_pi)
    print "Accuracy with math.pi: " + str(accuracy)

def main2(argv):
    if len(argv) != 1:
        sys.exit('Usage: pi.py <n>')

    print '\nComputing Pi v.01\n'

    a = 1.0
    b = 1.0/math.sqrt(2)
    t = 1.0/4.0
    p = 1.0

    for i in range(int(sys.argv[1])):
        at = (a+b)/2
        bt = math.sqrt(a*b)
        tt = t - p*(a-at)**2
        pt = 2*p
         
        a = at;b = bt;t = tt;p = pt

    my_pi = (a+b)**2/(4*t)
    accuracy = 100*(math.pi-my_pi)/my_pi

    print "Pi is approximately: " + str(my_pi)
    print "Accuracy with math.pi: " + str(accuracy)

def bbp(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
        k += 1
    return pi

def bellard(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k/(1024**k))*( Decimal(256)/(10*k+1) + Decimal(1)/(10*k+9) - Decimal(64)/(10*k+3) - Decimal(32)/(4*k+1) - Decimal(4)/(10*k+5) - Decimal(4)/(10*k+7) -Decimal(1)/(4*k+3))
        k += 1
    pi = pi * 1/(2**6)
    return pi

def chudnovsky(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi


def main(argv):
    if len(argv) != 2:
        sys.exit('Usage: BaileyBorweinPlouffe.py <prec> <n>')

    getcontext().prec = (int(sys.argv[1]))
    my_pi = bbp(int(sys.argv[2]))
    accuracy = 100*(Decimal(math.pi)-my_pi)/my_pi

    print "Pi is approximately " + str(my_pi)
    print "Accuracy with math.pi: " + str(accuracy)
     
if __name__ == "__main__":
    main(sys.argv[1:])
