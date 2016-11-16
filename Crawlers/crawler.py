
class Crawler(object):

    HalfWidth = 0
    HalfHeight = 0
    instances = []

    def __init__(self):
        self.position = self.rndPositionVector()
        self.velocity = PVector(0, 0)
        self.accel = PVector(0, 0)
        self.color = color(0, 0, 100)
        # This property keeps us from needing a global.
        self.imgColor = self.color
        self.instances.append(self)

    def rndPositionVector(self):
        x = int(random(-self.HalfWidth, self.HalfWidth))
        y = int(random(-self.HalfHeight, self.HalfHeight))
        return PVector(x, y)

    def update(self):
        # Image pixel's saturation becomes crawler's brightness.
        self.color = color(0, 0, saturation(self.imgColor))
        self.velocity = PVector.fromAngle(hue(self.imgColor))
        # Thanks to Shiffman's NOC!
        b = brightness(self.imgColor)
        if b <= 50:
            self.accel.add = b / -10
        else:
            self.accel.add = b / 10
        self.velocity.add(self.accel)
        self.position.add(self.velocity)
        self.display()

    def display(self):
        fill(self.color)
        # point(self.position.x, self.position.y)
        # print('self.position.x = {0}, self.position.y = {1}'
        #       .format(self.position.x, self.position.y))
        ellipse(self.position.x, self.position.y, 2, 2)
