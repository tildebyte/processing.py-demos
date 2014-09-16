"""
 * Creative Coding
 * Week 3, 04 - spinning top: curved motion with sin() and cos()
 * by Indae Hwang and Jon McCormack
 * Copyright (c) 2014 Monash University
 *
 * This sketch is the first cut at translating the motion of a spinning top
 * to trace a drawing path. This sketch traces a path using sin() and cos()
 *
"""
from getPaletteCSV import getPaletteCSV

from top import Top

Top.Palette = getPaletteCSV('Less-Angry_Rainbow_hex.csv')
top = None


def setup():
    size(800, 800)
    # Initial position in the center of the screen.
    top = Top(width / 2, height / 2)
    strokeWeight(1)
    smooth()


def draw():
    fill(255, 10)
    noStroke()
    rect(0, 0, width, height)
    top.move(width, height, radians(frameCount))
    top.drawMe()
