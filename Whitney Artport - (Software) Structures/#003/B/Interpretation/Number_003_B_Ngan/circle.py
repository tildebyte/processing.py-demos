class Circle(object):
    TableLength = int((TAU * 100) + 1)  # 628 - a full circle.
    sintable = [sin(i * 0.01) for i in range(TableLength)]
    costable = [cos(i * 0.01) for i in range(TableLength)]

    def __init__(self, locX, locY, radius, index):
        self.x = locX
        self.y = locY
        self.radius = radius
        self.diameter = self.radius * 2
        self.radiusSquared = self.radius * self.radius
        self.index = index
        self.speeds = [random(2), random(2), random(2)]
        self.accels = [random(0.5) - random(0.5),
                       random(0.5) - random(0.5),
                       random(0.5) - random(0.5)]
        self.over = True
        self.inx = 0
        self.iny = 0

    def getGrid(self, grid):
        sx = ceil((self.x - self.radius - grid.margin) / grid.gap)
        sy = ceil((self.y - self.radius - grid.margin) / grid.gap)
        numx = floor(self.diameter / grid.gap)
        numy = floor(self.diameter / grid.gap)
        for i in range(sx, sx + numx):
            if 0 <= i < grid.fieldSize:
                for k in range(sy, sy + numy):
                    if 0 <= k < grid.fieldSize:
                        if self.over:
                            x, y = grid.getLocation(i, k)
                            if (dist(self.x, self.y, x, y)
                                    < self.radius):
                                da = atan2(y - self.iny, x - self.inx)
                                if grid.field[i][k] < da:
                                    grid.field[i][k] += PI / 20
                                elif grid.field[i][k] > da:
                                    grid.field[i][k] -= PI / 20
        self.over = False

    def move(self, circles):
        angle = (Circle.getFunc('sin', self.speeds[0])
                 - Circle.getFunc('cos', self.speeds[1]))
        self.speeds[0] += self.accels[0]
        self.speeds[1] += self.accels[1]
        self.speeds[2] += self.accels[2]
        if angle < 0:
            angle += TAU
        elif angle >= TAU:
            angle -= TAU
        self.x += Circle.getFunc('sin', angle)
        self.y += Circle.getFunc('cos', angle)
        self.checkBounds()
        self.checkOverlap(circles)

    def checkBounds(self):
        if self.x > width:
            self.x = 0
        if self.x < 0:
            self.x = width
        if self.y > height:
            self.y = 0
        if self.y < 0:
            self.y = height

    def checkOverlap(self, circles):
        for other in circles:
            if other.index is not self.index:
                dx = other.x - self.x
                dy = other.y - self.y
                diameterSquared = dx**2 + dy**2
                diameter = sqrt(diameterSquared)
                if (diameter > self.radius + other.radius
                        or diameter < abs(self.radius - other.radius)):
                    continue # no solution
                a = atan2(dy, dx)
                self.repel(a + PI)
                other.repel(a)
                angle = ((self.radiusSquared - other.radiusSquared + diameterSquared)
                         / (2 * diameter))
                intersectX = self.x + angle * (other.x - self.x) / diameter
                intersectY = self.y + angle * (other.y - self.y) / diameter
                self.setState(intersectX, intersectY)
                other.setState(intersectX, intersectY)


    def repel(self, angle):
        self.x += Circle.getFunc('cos', angle) * 0.1
        self.y += Circle.getFunc('sin', angle) * 0.1

    def setState(self, intersectX, intersectY):
        self.inx = intersectX
        self.iny = intersectY
        self.over = True

    @staticmethod
    def getFunc(func, val):
        if val < 0:
            val += TAU
        if val >= TAU:
            val -= TAU
        val = min(TAU, max(0, val))  # 6.27
        if func == 'sin':
            return Circle.sintable[floor(val * 100)]
        elif func == 'cos':
            return Circle.costable[floor(val * 100)]
