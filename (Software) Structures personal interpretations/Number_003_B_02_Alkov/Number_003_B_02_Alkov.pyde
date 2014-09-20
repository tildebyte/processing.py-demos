'''
A surface filled with one hundred medium to small sized circles. Each
circle has a different size and direction, but moves at the same slow
rate.

Display the aggregate intersections of the circles.

Implemented by J. Tarbell <http://levitated.net>
8 April 2004
Processing v.68

Port to Processing.py/Processing 2.0 by Ben Alkov 10 July 2014
'''
from disc import Disc

# Object array.
discs = None

# Number of passes for SandPainters to render.
# Probably best not to tamper.
Passes = 11
NumDiscs = 100

def setup():
    global discs
    size(700, 700)
    ellipseMode(RADIUS)
    smooth(4)
    background(216, 233, 255)
    frameRate(24)

    # Make 100 discs, arranged linearly.
    discs = [Disc(i) for i in range(NumDiscs)]


def draw():
    fill(216, 233, 255, 40)
    rect(0, 0, width, height)

    # Move discs.
    for disc in discs:
        disc.move()
        disc.render(discs, Passes)
