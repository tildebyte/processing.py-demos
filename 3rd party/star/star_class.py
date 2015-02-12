class Star(object):
    """A collection of a varying number of identical isoceles triangles with
    a common base point. This object stores its own number of triangles,
    position, and color"""

    def __init__(self, numTris, fillColor, translation, rotation):
        # super(Star, self).__init__()
        self.numTris = numTris
        self.fillColor = fillColor
        self.translation = translation
        self.rotation = rotation
        self.tri = PShape()

    def update(self):
        for _ in range(self.numTris):
            rotate(TAU / self.numTris)
            shape(self.tri)
