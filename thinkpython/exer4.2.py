from swampy.TurtleWorld import *
import math

world = TurtleWorld()
n = 60

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n):
    for i in range(n):
        fd(t, length)
        lt(t, 360/n)

def circle(t, r):
    n = 60
    circumference = math.pi * 2 * r
    polygon(t, circumference/n, n)

def arc(t, r, angle):
    circumference = math.pi * 2 * r
    steps = int(1.0*angle/360 * n)
    for i in range(steps):
        fd(t, circumference/n)
        lt(t, 360/n)


bob = Turtle()
bob.delay = 0.01
# square(bob, 200)
# polygon(bob, 10, 60)
# circle(bob, 100)
# arc(bob, 100, 240)

for i in range(11):
    arc(bob, 200, 40)
    lt(bob,145)
    arc(bob, 200, 40)
    lt(bob,45)
    # c = raw_input()

wait_for_user()
