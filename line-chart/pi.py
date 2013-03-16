#!/usr/bin/env python

#  -*-  coding: utf-8  -*-
pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823"
pi = pi.replace(".", "")[:100]

# initialize result as dict
result = {str(x):0 for x in xrange(10)}

for i in xrange(100):
  result[pi[i]] += 1

# for i in result.items():
#   print i[0]

print sorted(result.items(), key=lambda t: t[1], reverse=True)

print result.items()
