class Segment(object):
    '''A Segment, which encapsulates its own position and color, and can draw
    itself'''

    def __init__(self, idx, color):
        self.idx = idx
        self.color = color
        self.loc = PVector(0.0, 0.0, 0.0)
        self.lineWidth = 0

    def calc(self, tentacleIndex, time):
        # This segment's visual offset is based on its location along the
        # tentacle ("further out" is "further back"), and the current time.
        offset = time - (self.idx * 0.03) - (tentacleIndex * 3)
        # Spherical coords.
        # New formula from http://acko.net/blog/js1k-demo-the-making-of
        # lon = (cos(offset + sin(offset * 0.31)) * 2
        lon = (cos(offset + sin(offset * 0.3)) * 2
               + sin(offset * 0.83) * 3
               + offset * 0.02)
        lat = (sin(offset * 0.7)
               # - cos(3 + offset * 0.23) * 3)
               - cos(3 + offset * 0.2) * 3)
        # The original worked within a coordinate system between -1 and 1. We
        # have to scale by a very large factor here.
        distance = sqrt(self.idx * 16500.0)
        # Convert to cartesian 3D.
        # http://acko.net/blog/js1k-demo-the-making-of
        self.loc.set(cos(lon) * cos(lat) * distance,
                     sin(lon) * cos(lat) * distance,
                     sin(lat) * distance)
        self.calcLineWidth(self.loc.z)

    def calcLineWidth(self, z):
        avoidzerodiv = 0
        if z == 0:
            avoidzerodiv = 1
        raw = self.idx / (z + avoidzerodiv)
        width = constrain(abs(raw), 0.01, 0.99)
        self.lineWidth = map(width, 0.01, 0.99, 3, 9)

    def drawSelf(self, other):
        stroke(self.color)
        strokeWeight(self.lineWidth)
        line(self.loc.x, self.loc.y, self.loc.z,
             other.loc.x, other.loc.y, other.loc.z)
