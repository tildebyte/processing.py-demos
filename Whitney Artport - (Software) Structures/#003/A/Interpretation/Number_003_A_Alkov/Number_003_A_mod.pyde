'''
    Modified
    Structure 3

    A surface filled with one hundred medium to small sized circles.
    Each circle has a different size and direction, but moves at the
    same slow rate.
    Display:
    A. The instantaneous intersections of the circles
    B. The aggregate intersections of the circles

    Implemented by Casey Reas <http://groupc.net>
    8 March 2004
    Processing v.68 <http://processing.org>

'''

NumCircles = 150
circles = None


def setup():
    size(1280, 720, P3D)
    frameRate(45)
    global circles
    # random x, y based on index value
    circles = [Circle(random(width), height / NumCircles * i,
                      (random(1, 6)) * 10, random(-0.7, 0.7),
                      random(-0.7, 0.7), i) for i in range(NumCircles)]
    ellipseMode(CENTER)
    background(173)


def draw():
    background(173)
    stroke(0)
    for i in range(NumCircles):
        circles[i].update()
    for i in range(NumCircles):
        circles[i].move()
    noFill()


class Circle:
    '''A circle object'''

    def __init__(self, x,  y,  r,  speed,  yspeed,  id):
        self.x = x
        self.y = y
        self.r = r
        self.r2 = self.r**2
        self.id = id
        self.speed = speed
        self.yspeed = yspeed

    def update(self):
        for i in range(NumCircles):
            if i != self.id:
                intersect(self, circles[i])

    def move(self):
        # Standard movement
        self.x += self.speed
        self.y += self.yspeed

        # Test against the *center* of the circle
        if self.speed > 0:
            if self.x > width + self.r:
                self.x = -self.r
        else:
            if self.x < -self.r:
                self.x = width + self.r

        if self.yspeed > 0:
            if self.y > height + self.r:
                self.y = -self.r
        else:
            if self.y < -self.r:
                self.y = height + self.r


def intersect(circleA, circleB):
    dx = circleA.x - circleB.x
    dy = circleA.y - circleB.y
    dSqr = dx**2 + dy**2
    hyp = sqrt(dSqr)
    # no intersection (one could be inside the other) OR co-incident
    if (hyp > circleA.r + circleB.r or
        hyp < abs(circleA.r - circleB.r)):
        return  # no solution

    a = (circleA.r2 - circleB.r2 + dSqr) / (2 * hyp)
    h = sqrt(circleA.r2 - a**2)
    x2 = circleA.x + a * (circleB.x - circleA.x) / hyp
    y2 = circleA.y + a * (circleB.y - circleA.y) / hyp
    paX = x2 + h * (circleB.y - circleA.y) / hyp
    paY = y2 - h * (circleB.x - circleA.x) / hyp
    pbX = x2 - h * (circleB.y - circleA.y) / hyp
    pbY = y2 + h * (circleB.x - circleA.x) / hyp
    distance = dist(paX, paY, pbX, pbY)
    stroke(255 - distance * 2)
    line(paX, paY, pbX, pbY)
