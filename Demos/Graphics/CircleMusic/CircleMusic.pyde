'''

'''

circles = []
tempo = 1


def setup():
    size(512, 512, P2D)
    stroke(255, 200)
    fill(255, 75)
    background(128)
    ellipseMode(RADIUS)


def draw():
    background(128)
    for c in circles:
        c.setRadius(c.getRadius() + tempo)
        c.display()


def mousePressed():
    makeCircle(mouseX, mouseY)


def makeCircle(x, y):
    for c in circles:
        distance = sqr((x - c.x)^2 + (y - c.y)^2)
    circles.append(Circle(x, y))


def compareCircles(current, other):
    # TODO: (1) @data use a list of distances saved as String. Exact matches..
    currentRadius = current.getRadius()
    otherRadius = other.getRadius()

    for c in circles:
        if currentRadius in c.distances:
            # and other circle matches storedDistance
            other.setRadius(0)
        else:
            if (currentRadius + otherRadius) >= storedDistances:
                if not currentRadius > otherRadius:
                    current.setRadius(currentRadius - tempo)

                current.setRadius(currentRadius + tempo)


class Circle():
    # TODO: (1)  @data - instance var list of distances [other hilite]
    def __init__(self, x, y):
        # if mod([x, y], some_value) = some other value, vary the pitch
        self.x = x
        self.y = y
        self.radius = 1
        # self.pitch = 0
        # TODO: (10)  @sound loudness based on the distance from the center of this
        #   circle to the center of the one which "popped" it.
        # self.loudness = 0
        # self.dur =

    def display(self):
        ellipse(self.x, self.y, 1, 1)
        ellipse(self.x, self.y, self.radius, self.radius)

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius
