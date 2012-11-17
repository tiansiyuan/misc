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

# def triangle(t, angle):
    

bob = Turtle()
bob.delay = 0.01
# square(bob, 200)
# polygon(bob, 10, 60)
# circle(bob, 100)
# arc(bob, 100, 240)

num = 9# 7 # 5
leng = 100
angle1 = 360 / num
angle2 = (180 - angle1) / 2
edge = 2 * math.cos(math.radians(angle2)) * leng

print num, angle1, angle2, edge

for i in range(num):
    fd(bob, leng)
    lt(bob, 180-angle2)
    fd(bob, edge)
    # c = raw_input()
    lt(bob, 180-angle2)
    fd(bob, leng)
    lt(bob, 180)
    # c = raw_input()

wait_for_user()
