class Point(object):
    def __init__(self, startX, startY):
        self.startX = startX
        self.startY = startY
        self.rnd = random(5, 30)
        self.diameter = map(self.rnd, 5, 30, 0.5, 2)
        if random(1) > 0.5:
            self.rt = True
        else:
            self.rt = False
        self.phi = random(360)
        self.x = 0
        self.y = 0

    def update(self, time):
        if self.rt:
            self.x = self._calc(self.startX, cos, time)
            self.y = self._calc(self.startY, sin, time)
        else:
            self.x = self._calc(self.startX, cos, -time)
            self.y = self._calc(self.startY, sin, -time)
        noStroke()
        fill(255)
        ellipse(self.x, self.y, self.diameter, self.diameter)


    def _calc(self, coord, func, time):
        return coord + self.rnd * func(radians(time * self.diameter + self.phi))
