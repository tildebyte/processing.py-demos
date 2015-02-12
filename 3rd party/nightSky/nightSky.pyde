# http://patakk.tumblr.com / nightSky
from point import Point


SketchWidth = 700
SketchHeight = 300
Point.HalfWidth = SketchWidth / 2
Point.HalfHeight = SketchHeight / 2
Point.HalfDist = dist(0, 0, Point.HalfWidth, Point.HalfHeight)
MagicNumber = dist(0, 0, 960, 540)
NumPoints = (500.0 * Point.HalfDist / MagicNumber)
Point.Limit = (160.0 * Point.HalfDist / MagicNumber)
points = []


def setup():
    global points
    size(SketchWidth, SketchHeight)
    background(0)
    smooth()
    strokeWeight(0.8)
    points = [Point(index) for index in range(NumPoints)]
    for _point in points:
        _point.setLines(points)


def draw():
    background(0)
    translate(Point.HalfWidth, Point.HalfHeight)
    for _point in points:
        _point.update(frameCount, points)
