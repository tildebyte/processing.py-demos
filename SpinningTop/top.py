class Top(object):
    '''A top.'''
    Palette = []
    MinDelta = 0.5
    MaxDelta = 1
    StrokeWeight = 1
    Radius = 0.5

    def __init__(self, x, y):
        self.pathX = x
        self.pathY = y
        self.deltaX = random(-1, 1)
        self.deltaY = random(-1, 1)
        self.tipX = 1
        self.tipY = 1
        self.handX = 1
        self.handY = 1

    def move(self, width, height, rads):
        # Calculate position.
        self.pathX += self.deltaX
        self.pathY += self.deltaY
        self.tipX = self.pathX + 100 * sin(rads)
        self.tipY = self.pathY + 100 * cos(rads)
        self.boundsCheck(width, height)
        # fill(0.7058)
        radius = 100 * sin(rads * 0.1)
        self.handX = self.tipX - radius * sin(rads * 3)
        self.handY = self.tipY - radius * cos(rads * 3)

    def boundsCheck(self, width, height):
        # When the shape hits the edge of the window, it reverses its
        #   direction and changes to a new random velocity.
        constrainedX = constrain(self.pathX, 0 + 100, width - 100)
        constrainedY = constrain(self.pathY, 0 + 100, height - 100)
        if constrainedX != self.pathX:
            self.pathX = constrainedX
            if self.deltaX < 0:
                self.deltaX = Top.deltaV()
            else:
                self.deltaX = -Top.deltaV()
        if constrainedY != self.pathY:
            self.pathY = constrainedY
            if self.deltaY < 0:
                self.deltaY = Top.deltaV()
            else:
                self.deltaY = -Top.deltaV()

    @staticmethod
    def deltaV():
        return random(Top.MinDelta, Top.MaxDelta)

    def drawMe(self):
        noStroke()
        # Color is derived via the angle from the "hand" point to the top's
        #   tip, and via the angle from the tip to the path.
        tipColor = Top.getColor(self.findAngle('tip'))
        handColor = Top.getColor(self.findAngle('hand'))
        fill(tipColor)
        ellipse(self.tipX, self.tipY, Top.Radius, Top.Radius)
        fill(handColor)
        ellipse(self.handX, self.handY, Top.Radius, Top.Radius)
        strokeWeight(Top.StrokeWeight)
        stroke(lerpColor(tipColor, handColor, 0.5))
        line(self.tipX, self.tipY, self.handX, self.handY)

    # For debug.
    def drawMeNot(self):
        noStroke()
        fill(0, 0, 255)
        ellipse(self.pathX, self.pathY, Top.Radius, Top.Radius)
        fill(0, 255, 0)
        ellipse(self.tipX, self.tipY, Top.Radius, Top.Radius)
        fill(255, 0, 0)
        ellipse(self.handX, self.handY, Top.Radius, Top.Radius)

    @classmethod
    def getColor(cls, angle):
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
