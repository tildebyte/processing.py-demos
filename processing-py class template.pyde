import random


class Class(object):
    ''' '''

    def __init__(self):
        self.x = width / 2
        self.y = height / 2

    def display(self):
        noStroke()
        fill(255, 10)
        ellipse(self.x, self.y, 16, 16)

    def step(self):
        sd = 60
        mean = 320
        xRand = random.gauss(0, 1)
        yRand = random.gauss(0, 1)
        self.x = sd * xRand + mean
        self.y = sd * yRand + mean
        self.x = constrain(self.x, 0, width - 1)
        self.y = constrain(self.y, 0, height - 1)
