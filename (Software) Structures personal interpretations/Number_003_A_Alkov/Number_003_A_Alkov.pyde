'''
Modified
Structure 3

A surface filled with one hundred medium to small sized circles.
Each circle has a different size and direction, but moves at the
same slow rate.
Display:
A. The instantaneous intersections of the circles
B. The aggregate intersections of the circles

Implemented by Casey Reas <http://groupc.net>
8 March 2004
Processing v.68 <http://processing.org>
'''
from circle import Circle

NumCircles = 150
circles = None


def setup():
    global circles
    size(1280, 720, P3D)
    # random x, y based on index value
    circles = [Circle(random(width), height / NumCircles * i,
                      (random(1, 6)) * 10, random(-0.7, 0.7),
                      random(-0.7, 0.7), i) for i in range(NumCircles)]
    smooth(4)
    ellipseMode(CENTER)
    background(173)


def draw():
    background(173)
    stroke(0)
    for circle in circles:
        circle.update(circles)
        circle.move()
    noFill()
