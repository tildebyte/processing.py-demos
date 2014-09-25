'''
A surface filled with one hundred medium to small sized circles.
Each circle has a different size and direction, but moves at the same
slow rate.

Display the aggregate intersections of the circles.

Implemented by William Ngan <http://metaphorical.net>
4 April 2004
Processing v.68 <http://processing.org>

Port to Processing.py/Processing 2.0 by Ben Alkov 5 September 2014
'''
from circle import Circle
from grid import Grid


grid = None
NumCircles = 10
circles = []
counter = 0
CirclePosition = 250
Radius = 40


def setup():
    global grid
    size(500, 500)
    # Init here because of sketch `width` & `height` being undefined prior to
    # this point.
    grid = Grid(TAU - PI / 3, 20, 3)


def draw():
    global counter
    background(50)
    stroke(255, 255, 255, 50)
    if frameCount % 5 == 0 and counter < NumCircles:
        circles.append(Circle(CirclePosition, CirclePosition, Radius, counter))
        counter += 1
    grid.update()
    for circle in circles:
        circle.move(circles)
        circle.getGrid(grid)
