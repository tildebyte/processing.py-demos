# PDE:
# add_library('hype')
# processing.py:
from hype.core.util import H
from hype.core.interfaces import HCallback
from hype.extended.behavior import HOscillator
from hype.extended.drawable import HCanvas
from hype.extended.drawable import HRect
from hype.extended.layout import HGridLayout
from hype.extended.util import HDrawablePool


from random import choice


rectRadius = 50
numSquares = 25
canvas = None
pool = None
color1 = 0x406B2B24  # #6B2B24
color2 = 0xc4831521  # #831521



def setup():
    size(568, 568)
    H.init(this).background(0xffE0DFE2)  # #E0DFE2
    smooth()
    canvas = H.add(HCanvas()).autoClear(False).fade(5)
    pool = HDrawablePool(numSquares)
    pool.autoParent(canvas)\
        .add(HRect()
             .size(rectRadius * 2)
             .noStroke())\
        .layout(HGridLayout()
                .startLoc(rectRadius * 2 - 20, rectRadius * 2 - 20)
                .spacing(rectRadius * 2 + 1, rectRadius * 2 + 1)
                .cols(5))\
        .onCreate(Callback())\
        .requestAll()


def draw():
    H.drawStage()


class Callback(HCallback):
    @staticmethod
    def run(drawable):
        drawable.anchorAt(H.CENTER)\
                .fill(choice([color1, color2]))
        HOscillator()\
            .target(drawable)\
            .property(H.ROTATION)\
            .range(-5, 5)\
            .speed(1)\
            .freq(4)\
            .currentStep(pool.currentIndex() * random(2, 25))
