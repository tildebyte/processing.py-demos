from segment import Segment

NumSegments = 12

class Tentacle(object):
    '''A Tentacle made of Segments.
    '''

    def __init__(self, idx, palette):
        self.idx = idx
        self.palette = palette
        self.segments = [Segment(i, lerpColor(palette[0], palette[1],
                                              i / (NumSegments / 1.0)))
                         for i in range(NumSegments)]

    def update(self, time):
        for s in self.segments:
            s.calc(self.idx, time)
            # Don't try to draw the last segment.
            if s.idx != len(self.segments) - 1:
                # Draw to the next segment.
                s.drawSelf(self.segments[s.idx + 1])
