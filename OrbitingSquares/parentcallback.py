'''
    `draw()` loop callback for the invisible parent `HGroup`s.
'''
from hype.core.util import H
from hype.core.interfaces import HCallback

import util


class ParentCallback(HCallback):
    @staticmethod
    def run(parent):
        # Pull one HRect from the pool of visible HRects.
        child = util.visiblePool.request()
        parent.noStroke()\
              .noFill()\
              .size(3)\
              .rotation(random(360))
        # In order for the object to rotate *on* the orbit, around the
        # *orbit's* center, we have to set its center to the center of the
        # orbit, and then calculate its position on the orbit based on the
        # child's position.
        parent.loc(util.centerX, util.centerY)\
              .anchor(abs(child.x() - util.centerX),
                      abs(child.y() - util.centerY))
        parent.add(child)
        # Move the child to the parent's center.
        child.locAt(H.CENTER)
        util.applyRotation(parent, 0.5, 0.01)
