# add_library('hype')
'''
    1. One hundred `HRect`
    2. Of randomly-selected size
    3. Each having semi-tranparent fill and stroke
    4. Each colored according to an underlying `HColorField`
    5. Each rotating around its own center with a randomly-selected speed and
       direction
    6. Randomly distributed around the circumference of
    7. One of several concentric circles
    8. All squares rotating at a randomly-selected speed and direction around
       a common center point

    Implementation by Ben Alkov 7-12 August 2014

'''
from hype.core.util import H
from hype.extended.colorist import HColorField
from hype.extended.drawable import HGroup
from hype.extended.drawable import HRect

import util

from parentcallback import ParentCallback
from rectcallback import RectCallback


def setup():
    size(800, 800)
    util.centerX = width / 2
    util.centerY = height / 2
    H.init(this).background(0xff595E6E)  # #595E6E
    smooth()
    util.colorfield = (HColorField(width, height)
                       .addPoint(0, util.centerY, 0xff001CDD, 0.7)  # #001CDD
                       .addPoint(width, util.centerY, 0xff71BB00, 0.7)  # #71BB00
                       .fillAndStroke())
    # No `requestAll()` for the visible HRects. They will be requested inside
    # the parent's callback.
    util.visiblePool.add(HRect())\
               .onCreate(RectCallback())
    util.parentPool.autoAddToStage()\
              .add(HGroup())\
              .onCreate(ParentCallback())\
              .requestAll()


def draw():
    H.drawStage()
