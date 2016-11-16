from random import normalvariate
from star import Star


class Follower(Star):

    """Ellipses with random color, location, and size, which follow the Stars"""
    # instances = []
    RadRange = (1, 8)  # Follower size range
    RadParms = [4.5, 0.75]
    ValRange = (13, 45)  # Brightness is based solely on Followers radius

    def __init__(self):
        super(self.__class__, self).__init__()
        self.color = self.setColor()

    def calcRedshift(self, hue, shift):
        h = hue - shift
        if h < 0 or h > 360:
            self.calcRedshift(360, abs(h))
        else:
            return h

    def setColor(self):
        # "Red-shift" closest's color
        H = self.calcRedshift(hue(self.closest.color), self.closestDistance)
        # rgb(98, 234, 203)
        S = saturation(self.closest.color) - 5
        B = self.mapColorComponent(self.ValRange)
        return color(H, S, B)
