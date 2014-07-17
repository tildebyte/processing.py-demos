class Circle(object):
    NumCollisions = 0  # Number of collisions in one frame
    NumConnections = 0  # Total number of collisions
    GravityAngle = 1  # Angle to gravity center in degrees
    GravityTheta = 1  # Angle to gravity center in radians
    TotalCircles = 0
    Gravity = 0
    CXV = 0
    CYV = 0

    def __init__(self, index, x, y, xv, yv):
        self.index = index
        self.x = x
        self.y = y
        self.radius = 2
        self.xv = xv
        self.yv = yv
        self.mightCollide = [1] * Circle.TotalCircles
        self.hasCollided = [1] * Circle.TotalCircles
        self.distances = [1] * Circle.TotalCircles
        self.angles = [1] * Circle.TotalCircles
        self.thetas = [1] * Circle.TotalCircles

    def behave(self, circles, sketchXMid, sketchYMid):
        self.move()
        self.areWeClose(circles)
        self.areWeColliding(circles)
        self.areWeConnected(circles)
        self.applyGravity(sketchXMid, sketchYMid)
        self.render(circles)
        self.reset()

    def areWeClose(self, others):
        for other in others:
            if self.index != other.index:
                if (abs(self.x - other.x) < 50
                        and abs(self.y - other.y) < 50):
                    self.mightCollide[other.index] = True
                else:
                    self.mightCollide[other.index] = False

    def areWeColliding(self, others):
        for other in others:
            if (self.mightCollide[other.index]
                    and self.index != other.index):
                self.distances[other.index] = dist(self.x, self.y,
                                                   other.x, other.y)
                if (self.distances[other.index]
                        < (self.radius + other.radius) * 1.1):
                    self.hasCollided[other.index] = True
                    other.hasCollided[self.index] = True
                    self.angles[other.index] = Circle.findAngle(self.x, self.y,
                                                                other.x, other.y)
                    self.thetas[other.index] = (-(self.angles[other.index] * PI)) / 180.0
                    Circle.CXV += (cos(self.thetas[other.index])
                                   * ((other.radius + self.radius) / 2.0))
                    Circle.CYV += (sin(self.thetas[other.index])
                                   * ((other.radius + self.radius) / 2.0))
                    Circle.NumCollisions += 1
        if Circle.NumCollisions > 0:
            self.xv = -Circle.CXV / Circle.NumCollisions
            self.yv = -Circle.CYV / Circle.NumCollisions
        Circle.CXV = 0.0
        Circle.CYV = 0.0

    def areWeConnected(self, others):
        maxDistance = 150
        for other in others:
            if (self.hasCollided[other.index]
                    and self.index != other.index):
                self.distances[other.index] = dist(self.x, self.y,
                                                   other.x, other.y)
                if self.distances[other.index] < maxDistance:
                    self.angles[other.index] = Circle.findAngle(self.x, self.y,
                                                                other.x, other.y)
                    self.thetas[other.index] = (-(self.angles[other.index] * PI)) / 180.0
                    Circle.CXV += cos(self.thetas[other.index]) * (self.radius / 8.0)
                    Circle.CYV += sin(self.thetas[other.index]) * (self.radius / 8.0)
                    Circle.NumConnections += 1
                else:
                    self.hasCollided[other.index] = False
                    other.hasCollided[self.index] = False
        if Circle.NumConnections > 0:
            self.xv += (Circle.CXV / Circle.NumConnections) / 4.0
            self.yv += (Circle.CYV / Circle.NumConnections) / 4.0
        Circle.CXV = 0.0
        Circle.CYV = 0.0
        self.radius = Circle.NumConnections * .85 + 2

    def applyGravity(self, sketchXMid, sketchYMid):
        Circle.GravityAngle = Circle.findAngle(self.x, self.y,
                                               sketchXMid, sketchYMid)
        Circle.GravityTheta = (-(Circle.GravityAngle * PI)) / 180
        self.xv += cos(Circle.GravityTheta) * Circle.Gravity
        self.yv += sin(Circle.GravityTheta) * Circle.Gravity

    def move(self):
        self.x += self.xv
        self.y += self.yv

    def render(self, others):
        noStroke()
        fill(0, 25)
        ellipse(self.x, self.y, self.radius, self.radius)
        fill(0 + self.radius * 10, 50)
        ellipse(self.x, self.y, self.radius * 0.5, self.radius * 0.5)
        fill(0 + self.radius * 10)
        ellipse(self.x, self.y, self.radius * 0.3, self.radius * 0.3)
        if Circle.NumCollisions > 0:
            noStroke()
            fill(0, 25)
            ellipse(self.x, self.y, self.radius, self.radius)
            fill(0, 55)
            ellipse(self.x, self.y, self.radius * 0.85, self.radius * 0.85)
            fill(0)
            ellipse(self.x, self.y, self.radius * 0.7, self.radius * 0.7)
        for other in others:
            if (self.hasCollided[other.index]
                    and self.index != other.index):
                with beginShape(LINE_LOOP):
                    xdist = self.x - other.x
                    ydist = self.y - other.y
                    stroke(0, 150 - self.distances[other.index] * 2.0)
                    vertex(self.x, self.y)
                    vertex(self.x - xdist * 0.25 + random(-1.0, 1.0),
                           self.y - ydist * 0.25 + random(-1.0, 1.0))
                    vertex(self.x - xdist * 0.5 + random(-3.0, 3.0),
                           self.y - ydist * 0.5 + random(-3.0, 3.0))
                    vertex(self.x - xdist * 0.75 + random(-1.0, 1.0),
                           self.y - ydist * 0.75 + random(-1.0, 1.0))
                    vertex(other.x, other.y)
                line (self.x, self.y, other.x, other.y);
        noStroke()

    @classmethod
    def reset(cls):
        Circle.NumCollisions = 0
        Circle.NumConnections = 0

    @classmethod
    def findAngle(cls, x1, y1, x2, y2):
        return 180 + (-(180 * (atan2(y1 - y2, x1 - x2))) / PI)
