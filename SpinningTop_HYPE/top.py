from hype.core.util import H
from hype.extended.drawable import HEllipse
from hype.extended.drawable import HPath


class Top(object):
    '''A top.'''
    Palette = []
    MinSpeed = 0.5
    MaxSpeed = 1.0
    StrokeWeight = 1
    Radius = 0.5

    def __init__(self, x, y):
        self.pathX = x
        self.pathY = y
        self.speedX = Top.newSpeed()
        self.speedY = Top.newSpeed()
        self.tipX = 1
        self.tipY = 1
        self.handX = 1
        self.handY = 1
        self.tipDrawable = (HEllipse(Top.Radius)
                            .noStroke()
                            .anchorAt(H.CENTER))
        self.handDrawable = (HEllipse(Top.Radius)
                             .noStroke()
                             .anchorAt(H.CENTER))
        self.lineDrawable = (HPath()
                             .strokeWeight(Top.StrokeWeight)
                             .strokeCap(ROUND))

    def update(self, width, height, rads):
        # Calculate position.
        self.pathX += self.speedX
        self.pathY += self.speedY
        self.tipX = self.pathX + 100 * (sin(rads))
        self.tipY = self.pathY + 100 * (cos(rads))
        self.boundsCheck(width, height)
        radius = 100 * sin(rads * 0.1)
        self.handX = self.tipX - radius * sin(rads * 3)
        self.handY = self.tipY - radius * cos(rads * 3)
        self.updateDrawables()

    def boundsCheck(self, width, height):
        # When the shape hits the edge of the window, it reverses its
        #   direction and changes to a new random velocity.
        constrainedX = constrain(self.pathX, 0 + 100, width - 100)
        constrainedY = constrain(self.pathY, 0 + 100, height - 100)
        if constrainedX != self.pathX:
            self.pathX = constrainedX
            if self.speedX < 0:
                self.speedX = Top.newSpeed()
            else:
                self.speedX = -Top.newSpeed()
        if constrainedY != self.pathY:
            self.pathY = constrainedY
            if self.speedY < 0:
                self.speedY = Top.newSpeed()
            else:
                self.speedY = -Top.newSpeed()

    @staticmethod
    def newSpeed():
        return random(Top.MinSpeed, Top.MaxSpeed)

    def updateDrawables(self):
        # Color is derived via the angle from the "hand" point to the top's
        #   tip, and via the angle from the tip to the path.
        tipColor = Top.getColor(self.findAngle('tip'))
        handColor = Top.getColor(self.findAngle('hand'))
        self.lineDrawable.stroke(lerpColor(tipColor, handColor, 0.5), 70)\
                         .strokeWeight(Top.StrokeWeight)\
                         .line(self.tipX, self.tipY, self.handX, self.handY)
        self.handDrawable.fill(handColor)\
                         .loc(self.handX, self.handY)
        self.tipDrawable.fill(tipColor)\
                        .loc(self.tipX, self.tipY)


    @staticmethod
    def getColor(angle):
        # Map the range of angles to the range of the entire palette.
        #         We retrieve the color as rgb.
        r, g, b = Top.Palette[int(map(angle, 0, TAU, 0, 945))].rgb

        # Convert color elements from `float` to `int`.
        return color(r * 255, g * 255, b * 255)

    def findAngle(self, which):
        # Return the normalized angle (in radians) between the "hand" location
        #   and the top location.
        if which == 'tip':
            return atan2(self.tipY - self.pathY, self.tipX - self.pathX) + PI
        elif which == 'hand':
            return atan2(self.handY - self.tipY, self.handX - self.tipX) + PI
