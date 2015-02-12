'''
OpenProcessing Tweak of *@*http:#www.openprocessing.org/sketch/153544*@*
'''

from __future__ import division
from ball import (Ball)


balls = None
NumBalls = 500  # The number of lines.
NumSources = 7  # The number of gravity points.
Sources = None
Ball.Radius = 200


def setup():
    global Sources, balls
    size(600, 600)
    frameRate(24)
    background(255)
    strokeWeight(0.5)
    noFill()
    # Gravity points initialize.
    Sources = [PVector(width / 2 + Ball.Radius * cos(i * TAU / NumSources),
                       height / 2 + Ball.Radius * sin(i * TAU / NumSources))
               for i in range(NumSources)]
    # Balls initialize.
    balls = [Ball(random(0, TAU))
             for _ in range(NumBalls)]


def draw():
    fadeToWhite(50)
    for ball in balls:
        ball.setSource(Sources)
        ball.move()
        ball.display()
    with pushStyle():
        fill(0)
        for source in Sources:
            ellipse(source.x, source.y, 10, 10)
    # filter(DILATE)


def fadeToWhite(opacity):
    with pushStyle():
        fill(255, opacity)
        noStroke()
        rect(0, 0, width, height)
