class Ball(object):
    CenterLocation = PVector(0, 0)
    Radius = 0

    def __init__(self, rndFactor):
        self.location = PVector(width / 2, height / 2)
        self.previousLocation = self.location.get()
        self.sourceLocation = PVector()
        self.speed = PVector(random(3, 15) * cos(rndFactor),
                             random(3, 15) * sin(rndFactor))
        self.acceleration = PVector(0, 0)

    def move(self):
        self.acceleration = PVector.sub(self.sourceLocation, self.location)
        self.acceleration.normalize()
        self.acceleration.mult(PVector.dist(self.sourceLocation, self.location)
                               **2 / 100000.0)
        self.speed.add(self.acceleration)
        self.location.add(self.speed)
        if PVector.dist(Ball.CenterLocation, self.location) < Ball.Radius:
            self.speed.mult(0.9)

    def display(self):
        # if self.previousLocation.mag() < 10000:
        with pushStyle():
            c = color(map(PVector.dist(self.location, self.sourceLocation),  # R
                          Ball.Radius, Ball.Radius * 1.2,
                          255, 64),
                      self.acceleration.mag() * 100,  # G
                      map(PVector.dist(self.location, self.sourceLocation),  # B
                          0, Ball.Radius,
                          0, 128))
            stroke(c)

            # Fast is narrow.
            strokeWeight(1 / (self.speed.mag() + 1) * 10)
            line(self.previousLocation.x, self.previousLocation.y,
                 self.location.x, self.location.y)
        self.previousLocation.set(self.location)

    def setSource(self, Sources):
        # Each 3fr, change gravity point
        index = (int(frameCount / frameRate * 3) + 1) % len(Sources)
        self.sourceLocation.set(Sources[index])
