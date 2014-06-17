class Circle(object):
    '''A circle object'''

    def __init__(self, centerX, centerY, radius, xspeed, yspeed, index):
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius
        self.rSqr = self.radius**2
        self.index = index
        self.xspeed = xspeed
        self.yspeed = yspeed

    def update(self, circles):
        for circle in circles:
            if circle.index != self.index:
                intersect(self, circle)

    def makepoint(self):
        stroke(0)
        point(self.centerX, self.centerY)

    def move(self):
        self.centerX += self.xspeed
        self.centerY += self.yspeed
        if self.xspeed > 0 and self.centerX > width + self.radius:
                self.centerX = -self.radius
        elif self.centerX < -self.radius:
                self.centerX = width + self.radius
        if self.yspeed > 0 and self.centerY > height + self.radius:
                self.centerY = -self.radius
        elif self.centerY < -self.radius:
                self.centerY = height + self.radius
