from random import randrange


class Ball(object):
    CenterLocation = PVector(0, 0)
    Radius = 0

    def __init__(self, speed, Sources):
        self.targetLocation = Sources[randrange(len(Sources))]
        self.location = PVector(width / 2, height / 2)
        self.previousLocation = PVector(99999, 99999)
        self.speed = speed
        self.acceleration = PVector(0, 0)

    def move(self):
        self.acceleration = PVector.sub(self.targetLocation, self.location)
        self.acceleration.normalize()
        self.acceleration.mult(PVector.dist(self.targetLocation,
                                            self.location)**2 / 100000)
        self.speed.add(self.acceleration)
        self.location.add(self.speed)
        if PVector.dist(Ball.CenterLocation, self.location) < Ball.Radius:
            self.speed.mult(0.9)

    def display(self):
        if self.previousLocation.mag() < 10000:
            with pushStyle():
                c = color(map(PVector.dist(self.location, self.targetLocation),  # R
                              Ball.Radius, Ball.Radius * 1.2,
                              255, 64),
                          self.acceleration.mag() * 100,  # G
                          map(PVector.dist(self.location, self.targetLocation),  # B
                              0, Ball.Radius,
                              0, 128))
                stroke(c)

                # Fast is narrow.
                strokeWeight(1 / (self.speed.mag() + 1) * 10)
                line(self.previousLocation.x, self.previousLocation.y,
                     self.location.x, self.location.y)
        self.previousLocation.set(self.location)

    def reset(self, Sources):
        # Each 3fr, change gravity point.
        self.targetLocation.set(Sources[int((frameCount / frameRate * 3) + 1)
                                % len(Sources)])
