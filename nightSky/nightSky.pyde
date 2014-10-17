# http://patakk.tumblr.com / nightSky
from point import Point
# from line import Line


points = []
lines = []
NumPoints = 0
Limit = 0
HalfWidth = 0
HalfHeight = 0
HalfDist = 0
I_Dont_Know_What_This_Is = dist(0, 0, 960, 540)

def setup():
    global points, HalfWidth, HalfHeight, HalfDist, NumPoints, Limit
    size(700, 300)
    background(0)
    smooth()
    strokeWeight(0.8)
    HalfWidth = width / 2
    HalfHeight = height / 2
    HalfDist = dist(0, 0, HalfWidth, HalfHeight)
    NumPoints = (500.0 * HalfDist / I_Dont_Know_What_This_Is)
    Limit = (160.0 * HalfDist / I_Dont_Know_What_This_Is)
    # n = 0
    # noiseSeed(5)
    # randomSeed(1200)
    # makePoint()
    points = [makePoint() for _ in range(NumPoints)]
    for point1 in points:
        x1 = point1.startX
        y1 = point1.startY
        for point2 in points:
            x2 = point2.startX
            y2 = point2.startY
            if dist(x1, y1, x2, y2) < Limit / 3:
                lines.append(PVector(points.index(point1),
                                     points.index(point2)))

def makePoint():
    while True:
        randX = random(HalfWidth * 0.74) + random(40)
        randY = random(HalfHeight * 0.84) + random(40)
        angle = random(2 * PI)
        startX = randX * cos(angle)
        startY = randY * sin(angle)
        dx = map(startX,
                 0, HalfWidth, 0, 1.15)
        dy = map(startY,
                 0, HalfHeight, 0, 1.35)
        prob = pow(2.72, -(dx**2 * 2 + dy**2 * 2))
        if random(1) < prob:
            return(Point(startX, startY))


def draw():
    background(0)
    translate(HalfWidth, HalfHeight)
    for _point in points:
        _point.update(frameCount)
    for _line in lines:
        x1 = points[int(_line.x)].x
        y1 = points[int(_line.x)].y
        x2 = points[int(_line.y)].x
        y2 = points[int(_line.y)].y
        plusX = x1 + x2 / 2
        plusY = y1 + y2 / 2
        mouseWrapX = mouseX - HalfWidth
        mouseWrapY = mouseY - HalfHeight
        amp = (map(dist(plusX, plusY, 0, 0),
                   0, HalfDist, 2, 8))
        distance = (map(noise(plusX * 0.03, plusY * 0.03),
                        0, 1, 5, Limit / 2))
        if dist(plusX, plusY, mouseWrapX, mouseWrapY) < Limit:
            distance = (distance * map(dist(plusX, plusY, mouseWrapX, mouseWrapY),
                                       0, Limit, amp, 1))
        if dist(x1, y1, x2, y2) < distance:
            opacity = map(dist(x1, y1, x2, y2),
                          0, distance, 85, 0)
            stroke(255, opacity)
            line(x1, y1, x2, y2)
