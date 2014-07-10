class Ball(object):
    EdgeBuffer = 200

    def __init__(self, index):
        self.index = index
        self.origin = PVector(random(Ball.EdgeBuffer, width - Ball.EdgeBuffer),
                              random(Ball.EdgeBuffer, height - Ball.EdgeBuffer))
        self.radius = random(50.0, 150.0)
        self.location = PVector(self.origin.x + self.radius, self.origin.y)
        if random(1) > 0.5:
            self.direction = -1
        else:
            self.direction = 1
        self.offset = random(TAU)
        self.theta = 0.0
        self.size = 10.0
        self.distanceLimit = 60

    def run(self, balls):
        self.move()
        self.display()
        self.lineBetween(balls)

    def move(self):
        self.location.x = self.origin.x + sin(self.theta + self.offset) * self.radius
        self.location.y = self.origin.y + cos(self.theta + self.offset) * self.radius
        # 0.02615 is sine of 1.5 degrees
        self.theta += (0.02615 * self.direction)

    def display(self):
        noStroke()
        for i in range(self.size, 0, -2):
            fill(255, int(map(i, self.size, 2, 0, 200)))
            ellipse(self.location.x, self.location.y, i, i)

    def lineBetween(self, balls):
        for ball in balls:
            if self.index is not ball.index:
                distance = self.location.dist(ball.location)
                if 0 < distance < self.distanceLimit:
                    stroke(0x96ffffff)
                    line(self.location.x, self.location.y,
                         ball.location.x, ball.location.y)
