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
sketchX = 600  # self.x dimension of applet
sketchY = 600  # self.y dimension of applet
sketchXMid = sketchX / 2  # self.x midpoint of applet
sketchYMid = sketchY / 2  # self.y midpoint of applet
Circle.TotalCircles = 100  # total number of circles
Circle.Gravity = 0.075  # Strength of gravitational pull
circles = [Circle(i, 0, 0, 0, 0)  # Circle object list
           for i in range(Circle.TotalCircles)]


# ****************************************************************************
# SETUP FUNCTION
# ****************************************************************************
def setup():
    size(600, 600)
    background(255)
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
    background(255)
    for circle in circles:
        circle.behave(circles, sketchXMid, sketchYMid)


def createCircles():
    angleOffset = random(360)
    for circle in circles:
        circle.xPos, circle.yPos = initCirclePos(circle.index, angleOffset,
                                                 random(10))
        circle.xv = 0
        circle.yv = 0


def initCirclePos(index, angleOffset, rand):
    initRadius = 150
    initAngle = index * 3.6 + angleOffset + rand
    initTheta = (-((initAngle) * PI)) / 180
    initxv = cos(initTheta) * initRadius
    inityv = sin(initTheta) * initRadius
    return sketchXMid + initxv, sketchYMid + inityv


def mouseReleased():
    createCircles()
