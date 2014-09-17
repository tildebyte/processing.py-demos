'''
    `draw()` loop callback for the visible squares.
'''
from hype.core.util import H
from hype.core.interfaces import HCallback

import util


class RectCallback(HCallback):
    @staticmethod
    def run(drawable):
        # Position this HRect at a random position on an orbit randomly chosen
        # from a set of four.
        creationX, creationY = util.positionOnOrbit()
        drawable.strokeWeight(2)\
                .stroke(0xff000000, 196)\
                .fill(0xff000000, 100)\
                .size(random(22, 38))\
                .rounding(2)\
                .rotation(random(360))\
                .loc(creationX, creationY)\
                .anchorAt(H.CENTER)
        util.colorfield.applyColor(drawable)
        # Apply a rotation with random speed and direction. This causes
        # the HRect to rotate around *its* center.
        util.applyRotation(drawable, 4.0, 0.5)
