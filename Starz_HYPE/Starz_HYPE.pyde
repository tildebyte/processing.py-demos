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
from tricallback import TriCallback


def setup():
    size(512, 512)
    util.centerX = width / 2
    util.centerY = height / 2
    frameRate(30)
    H.init(this).background(0)  # #000000
    smooth()
    # No `requestAll()` for the visible HRects. They will be requested inside
    # the parent's callback.
    util.visiblePool.add(HRect())\
               .onCreate(TriCallback())
    util.parentPool.autoAddToStage()\
              .add(HGroup())\
              .onCreate(ParentCallback())\
              .requestAll()


def draw():
    H.drawStage()
    # saveFrame('C:/Users/IBM_ADMIN/Documents/frames/####.tif')
    # if frameCount == 900:
    #     exit()
