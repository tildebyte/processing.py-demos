'''
`draw()` loop callback for the visible tris.
'''
from hype.core.util import H
from hype.core.interfaces import HCallback

import util


class TriCallback(HCallback):
    @staticmethod
    def run(drawable):
        # Position this HTri around its parent's center, at an angle based on
        # its index.
        # fill(random(288, 360), random(100, 255), random(51, 153), random(5, 15))
        drawable.noStroke()\
                .fill(0xff000000, 100)\
                .rotation(TAU / self.index)\
                .loc(0, 0)\
                .anchorAt(H.CENTER_BOTTOM)
