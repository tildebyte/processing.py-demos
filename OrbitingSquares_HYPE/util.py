'''
Globals and helper methods.
'''
from hype.extended.behavior import HRotate
from hype.extended.util import HDrawablePool

from random import randint


colorfield = None
centerX = None
centerY = None
visiblePool = HDrawablePool(100)
parentPool = HDrawablePool(100)


def positionOnOrbit():
    '''
    Generate a random position on the circumference of the orbit chosen for
    this item.
    '''
    angle = random(TAU)
    # `randint` slightly offsets the position so we don't end up with the
    # visible HRects orbiting on *exact* circles.
    radius = chooseOrbit() + randint(0, int(width / 23))
    createX = centerX + (cos(angle) * radius)  # `angle` *must* be radians.
    createY = centerY + (sin(angle) * radius)  #
    return createX, createY


def chooseOrbit():
    '''
    Randomly choose an orbit, based on a set of weights.
    The returns can be adjusted to account for a larger / smaller sketch size.
    '''
    chance = random(1)
    if chance < 0.18:
        return width / 8
    elif chance < 0.50:
        return width / 4
    elif chance < 0.78:
        return width / 2.46
    elif chance < 1.0:
        return width / 1.7777


def applyRotation(obj, speed, tolerance):
    '''
    Attach an HRotate to the given object, calling `avoidZero` to set the
    speed (angular speed in degrees per draw()).
    '''
    HRotate(obj, avoidZero(speed, tolerance))


# This is specifically used to avoid zero or synchronous rotation. We want all
# visible HRects to *appear* to rotate "in place".
def avoidZero(limit, tolerance):
    '''
    Return a random value in the range from `-limit` to strictly less than
    `limit`, excluding the inner range +/-`tolerance` (and, logically, zero as
    well).
    '''
    value = random(-limit, limit)
    while -tolerance < value < tolerance:
        value = random(-limit, limit)
        continue
    return value
