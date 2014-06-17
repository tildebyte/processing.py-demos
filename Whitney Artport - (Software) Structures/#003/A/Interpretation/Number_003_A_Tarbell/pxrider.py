# Pixel Rider object.
class PxRider(object):

    def __init__(self):
        self.theta = random(TAU)
        self.deltaV = 0.0
        self.charge = 0

    def move(self, x, y, radius):
        # Add velocity to theta.
        self.theta = (self.theta + self.deltaV + PI) % TAU - PI
        self.deltaV += random(-0.001, 0.001)

        # Apply friction brakes.
        if abs(self.deltaV) > 0.02:
            self.deltaV *= 0.9

        # Draw.
        px = x + radius * cos(self.theta)
        py = y + radius * sin(self.theta)
        color = get(px, py)
        if brightness(color) > 48:
            glowpoint(px, py)
            self.charge = 164
        else:
            stroke(self.charge)
            point(px, py)
            self.charge *= 0.98
