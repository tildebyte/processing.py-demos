from segment import Segment


class Tentacle(object):
    '''A Tentacle made of Segments.
    '''
    # Factor to determine the distance between Segments.
    AltitudeOffset = 1

    def __init__(self, timeOffset, palette):
        self.timeOffset = timeOffset
        self.palette = palette
        self.segments = [Segment(i, i,  # Second `i` is tickOffset.
                                 Tentacle.AltitudeOffset * i + i,
                                 self.palette[i])
                         for i in range(5)]

    def update(self, time, Tick, sphereRadius):
        for segment in self.segments:
            segment.calc((time - self.timeOffset) -
                         (segment.tickOffset * Tick),
                         sphereRadius)
            # Don't try to draw the last segment.
            if segment.id is not len(self.segments) - 1:
                # Draw to the next segment.
                segment.drawSelf(self.segments[segment.id + 1])
