from random import normalvariate


class Star(object):

    """Ellipses with random color, location, and size"""
    # Ideally, these would be something like `Sketch.HalfWidth`, or, even
    #    better, would be available here from the main `pyde` namespace.
    HalfWidth = 0
    HalfHeight = 0
    instances = []
    RadRange = (9, 50)  # Star size range
    # Seems to give the distribution I want. RadParms[0] is distribution mean,
    #    RadParms[1] is std.
    RadParms = [30, 8]
    HueRange = (37, 226)
    SatRange = (75, 50)
    ValRange = (75, 100)  # Yeah, I know. Technically it's "brightness".

    def __init__(self):
        self.radius = self.randomRad()
        self.loc = self.makeRandXY()
        self.loc = self.randomLoc(self.loc)
        if self.instances:
            # Also sets distance to closest star
            self.closest, self.closestDistance = self.findClosestStar()
            # print('closest.color h is {0}, s is {1}, b is {2}'
            #       .format(hue(self.closest.color),
            #               saturation(self.closest.color),
            #               brightness(self.closest.color)))
        if not getattr(self, 'color', False):
            self.color = self.setColor()
        self.instances.append(self)

    def randomRad(self):
        return int(normalvariate(self.RadParms[0], self.RadParms[1]))

    def makeRandXY(self):
        x = int(random(-self.HalfWidth, self.HalfWidth))
        y = int(random(-self.HalfHeight, self.HalfHeight))
        return (x, y)

    def randomLoc(self, coord):
        for i in self.instances:
            if i is not None:
                print('x is {0}, y is {1}, i.loc is {2}'
                      .format(coord[0], coord[1], i.loc))
                if (dist(coord[0], coord[1], i.loc[0], i.loc[1]) >
                        (i.radius + self.radius)):
                    return coord
                coord = self.makeRandXY()
                coord = self.randomLoc(coord)

    # This isn't *currently* used in this class, but might be if e.g. animation
    # is added later.
    def findClosestStar(self):
        s = None
        d = 999999
        for i in self.instances:
            i_dist = dist(self.loc[0], self.loc[1], i.loc[0], i.loc[1])
            if i_dist < d:
                s = i
                d = i_dist
        return s, d

    def mapColorComponent(self, range_):
        return map(self.radius,
                   self.RadRange[0], self.RadRange[1],
                   range_[0], range_[1])

    def setColor(self):
        H = self.mapColorComponent(self.HueRange)
        S = self.mapColorComponent(self.SatRange)
        B = self.mapColorComponent(self.ValRange)
        return color(H, S, B)

    def update(self):
        self.display()

    def display(self):
        fill(self.color)
        ellipse(self.loc[0], self.loc[1], self.radius, self.radius)
