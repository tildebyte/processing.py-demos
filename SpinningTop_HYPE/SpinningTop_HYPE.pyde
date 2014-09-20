'''
Adapted from:
    Creative Coding
    Week 3, 04 - spinning top: curved motion with sin() and cos()
    by Indae Hwang and Jon McCormack
    Copyright (c) 2014 Monash University

    This sketch is the first cut at translating the motion of a spinning top
    to trace a drawing path. This sketch traces a path using sin() and cos()

and ported to Processing.py/Processing 2.1/HYPE
by Ben Alkov, 30 July - 8 Sept 2014

The only thing left from the original sketch is the math describing the motion.
'''

from hype.core.util import H
from hype.extended.drawable import HCanvas

from getPaletteCSV import getPaletteCSV

from top import Top


Top.Palette = getPaletteCSV('Less-Angry_Rainbow_hex.csv')
Top.StrokeWeight = 2
Top.Radius = 1.5
top = None


def setup():
    global top
    size(512, 512, OPENGL)
    frameRate(30)
    H.init(this).background(0xff000000)
    smooth()
    canvas = H.add(HCanvas()).autoClear(False).fade(1)
    # Initial position in the center of the screen.
    top = Top(width / 2, height / 2)
    canvas.add(top.lineDrawable)
    canvas.add(top.handDrawable)
    canvas.add(top.tipDrawable)


def draw():
    top.update(width, height, radians(frameCount))
    H.drawStage()
    # saveFrame('C:/Users/IBM_ADMIN/Documents/frames/####.tif')
    # if frameCount == 900:
    #     exit()
