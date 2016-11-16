"""
Handles.

Click and drag the white boxes to change their position.
"""
from handle import Handle


def setup():
    size(640, 360)
    num = height / 15
    hsize = 10
    for i in range(num):
        Handle(width / 2, 10 + i * 15, 50 - hsize / 2, 10)


def draw():
    background(153)
    for h in Handle.handles:
        h.update()
        h.display()
    fill(0)
    rect(0, 0, width / 2, height)


def mouseReleased():
    for h in Handle.handles:
        h.releaseEvent()
