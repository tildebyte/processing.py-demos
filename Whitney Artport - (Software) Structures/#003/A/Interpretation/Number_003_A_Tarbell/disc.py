from pxrider import PxRider


# Disc object.
class Disc(object):
    def __init__(self, index, centerX, centerY, vx, vy, destinationRadius):
        # Identifier.
        self.index = index

        # Position.
        self.centerX = centerX
        self.centerY = centerY

        # Velocity.
        self.vx = vx
        self.vy = vy

        # Radius.
        self.destinationRadius = destinationRadius
        self.radius = 0

        # Create pixel riders.
        maxRiders = 40
        self.pxRiders = [PxRider() for _ in range(maxRiders)]

    def drawSelf(self):
        stroke(0, 50)
        noFill()
        ellipse(self.centerX, self.centerY, self.radius, self.radius)

    def render(self, discs):
        # Find intersecting points with all ascending discs.
        for disc in discs:
            if disc.index > self.index:
                # Find distance to other disc.
                dx = disc.centerX - self.centerX
                dy = disc.centerY - self.centerY
                d = sqrt(dx**2 + dy**2)

                # Intersection test.
                if d < (disc.radius + self.radius):
                    # Complete containment test.
                    if d > abs(disc.radius - self.radius):
                        # Find solutions.
                        a = (self.radius**2 - disc.radius**2 + d**2) / (2 * d)
                        p2x = self.centerX + a * (disc.centerX - self.centerX) / d
                        p2y = self.centerY + a * (disc.centerY - self.centerY) / d
                        h = sqrt(self.radius**2 - a**2)
                        p3ax = p2x + h * (disc.centerY - self.centerY) / d
                        p3ay = p2y - h * (disc.centerX - self.centerX) / d
                        p3bx = p2x - h * (disc.centerY - self.centerY) / d
                        p3by = p2y + h * (disc.centerX - self.centerX) / d

                        # p3a and p3B may be identical - ignore self case (for now).
                        stroke(255)
                        point(p3ax, p3ay)
                        point(p3bx, p3by)

    def move(self):
        # Add velocity to position.
        self.centerX += self.vx
        self.centerY += self.vy
        bound = width + self.radius * 2

        # Bound check.
        if self.centerX + self.radius < 0:
            self.centerX += bound
        if self.centerX - self.radius > width:
            self.centerX -= bound
        if self.centerY + self.radius < 0:
            self.centerY += bound
        if self.centerY - self.radius > width:
            self.centerY -= bound

        # Increase to destination radius.
        if self.radius < self.destinationRadius:
            self.radius += 0.1

    def renderPxRiders(self):
        for pxRider in self.pxRiders:
            pxRider.move(self.centerX, self.centerY, self.radius)
