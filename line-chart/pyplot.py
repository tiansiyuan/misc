#!/usr/bin/env python

import matplotlib.pyplot as pyplot

xs = (1, 2, 3, 4, 5)
ys = (1, 2, 3, 4, 5)
pyplot.plot(xs, ys)
scale = 'log'
pyplot.xscale(scale)
pyplot.yscale(scale)
pyplot.title('')
pyplot.xlabel('n')
pyplot.ylabel('run time (s)')
pyplot.show()
