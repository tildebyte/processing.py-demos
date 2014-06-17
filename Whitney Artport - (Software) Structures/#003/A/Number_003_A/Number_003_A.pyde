'''
    Structure #003A

    A surface filled with one hundred medium to small sized circles. Each
    circle has a different size and direction, but moves at the same slow
    rate.

    Display the instantaneous intersections of the circles.

    Implemented by Casey Reas
    8 March 2004
    Processing v.68

    Port to Processing.py/Processing 2.0 by Ben Alkov 8 May 2014
'''
from circle import Circle

NumCircles = 100
circles = None


def setup():
    size(800, 600)
    circles = [Circle(random(width), height / NumCircles * i,
                      (random(1, 6)) * 10, random(-1.0, 1.0),
                      random(-1.0, 1.0), i) for i in range(NumCircles)]
    ellipseMode(CENTER)
    background(255)


def draw():
    background(255)
    stroke(0)
    for circle in circles:
        circle.update()
        circle.move()
        circle.makepoint()
    noFill()


def intersect(circleA, circleB):
    dx = circleA.centerX - circleB.centerX
    dy = circleA.centerY - circleB.centerY
    dSqr = dx**2 + dy**2
    diameter = sqrt(dSqr)
    if diameter > circleA.radius + circleB.radius or diameter < abs(circleA.radius - circleB.radius):
        return  # no solution
    a = (circleA.rSqr - circleB.rSqr + dSqr) / (2 * diameter)
    h = sqrt(circleA.rSqr - a**2)
    x2 = circleA.centerX + a * (circleB.centerX - circleA.centerX) / diameter
    y2 = circleA.centerY + a * (circleB.centerY - circleA.centerY) / diameter
    paX = x2 + h * (circleB.centerY - circleA.centerY) / diameter
    paY = y2 - h * (circleB.centerX - circleA.centerX) / diameter
    pbX = x2 - h * (circleB.centerY - circleA.centerY) / diameter
    pbY = y2 + h * (circleB.centerX - circleA.centerX) / diameter
    stroke(255 - dist(paX, paY, pbX, pbY) * 4)
    line(paX, paY, pbX, pbY)
