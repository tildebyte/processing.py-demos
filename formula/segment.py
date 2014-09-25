class Segment(object):
    '''A Segment, which encapsulates its own position and color, and can draw
    itself'''

    def __init__(self, index, tickOffset, altitude, lineColor):
        self.index = index
        # A "magic" number. 12 just seems to look good.
        self.tickOffset = tickOffset * 12
        #  Effectively, the distance between segments.
        self.altitude = altitude
        self.lineColor = lineColor
        self.location = PVector(0.0, 0.0, 0.0)

    def calc(self, time, sphereRadius):
        # New formula from http://acko.net/blog/js1k-demo-the-making-of
        # Spherical coords.
        lon = cos(time + sin(time * 0.31)) * 2 + sin(time * 0.83) * 3 + time * 0.02
        lat = sin(time * 0.7) - cos(3 + time * 0.23) * 3
        # Convert to cartesian 3D.
        # http://acko.net/blog/js1k-demo-the-making-of
        self.location.set(cos(lon) * cos(lat) * (sphereRadius + self.altitude),
                          sin(lon) * cos(lat) * (sphereRadius + self.altitude),
                          sin(lat) * (sphereRadius + self.altitude))

    def drawSelf(self, other):
        stroke(self.lineColor)
        line(self.location.x, self.location.y, self.location.z,
             other.location.x, other.location.y, other.location.z)
