'''
A surface filled with one hundred medium to small sized circles.
Each circle has a different size and direction, but moves at the same
slow rate.

Display the instantaneous intersections of the circles

Implemented by Robert Hodgin <http://flight404.com>
6 April 2004
Processing v.68 <http://processing.org>

Port to Processing.py/Processing 2.0 by Ben Alkov 17 July 2014
'''
from circle import Circle


# ****************************************************************************
# INITIALIZE VARIABLES
# ****************************************************************************
sketchX = 600  # x dimension of sketch.
sketchY = 600  # y dimension of sketch.
sketchXMid = sketchX / 2  # x midpoint of sketch.
sketchYMid = sketchY / 2  # y midpoint of sketch.
TotalCircles = 100  # Total number of circles.
Circle.BgColor = color(255)
Circle.FgColor = color(0)
circles = None

# ****************************************************************************
# SETUP FUNCTION
# ****************************************************************************
def setup():
    size(sketchX, sketchY)
    background(Circle.BgColor)
    smooth()
    colorMode(RGB, 255)
    ellipseMode(RADIUS)
    noStroke()
    frameRate(30)
    createCircles()


# ****************************************************************************
# MAIN LOOP FUNCTION
# ****************************************************************************
def draw():
    background(Circle.BgColor)
    for circle in circles:
        circle.behave(circles, sketchXMid, sketchYMid)


def createCircles():
    angleOffset = random(360)
    initRadius = 150
    circles = []
    for i in range(TotalCircles):
        xPos, yPos = initCirclePos(i, angleOffset, initRadius)
        circles.append(Circle(i, xPos, yPos, 0, 0, TotalCircles))


def initCirclePos(index, angleOffset, initRadius):
    initTheta = radians(index * 3.6 + angleOffset + random(10))
    initXVel = cos(initTheta) * initRadius
    initYVel = sin(initTheta) * initRadius
    return sketchXMid + initXVel, sketchYMid + initYVel


def mousePressed():
    createCircles()
