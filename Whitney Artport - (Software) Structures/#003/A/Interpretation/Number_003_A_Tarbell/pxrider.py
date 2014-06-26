# Pixel Rider object.
class PxRider(object):

    def __init__(self):
        self.theta = random(TAU)
        self.deltaV = 0.0
        self.charge = 0

    # Methods.
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
        # color = get(px, py)
        loadPixels()
        color = pixels[int(px) + int(py) * height]
        if brightness(color) > 48:
            self.glowpoint(px, py)
            self.charge = 164
        else:
            stroke(self.charge)
            point(px, py)
            self.charge *= 0.98

    def tpoint(x, y, myColor, trans):
        # Place translucent point.
        # color = get(x, y)
        loadPixels()
        color = pixels[x + y * height]
        r = red(color) + (red(myColor) - red(color)) * trans
        g = green(color) + (green(myColor) - green(color)) * trans
        b = blue(color) + (blue(myColor) - blue(color)) * trans
        stroke(color(r, g, b))
        point(x, y)

    def glowpoint(px, py):
        for i in range(-2, 3):
            for j in range(-2, 3):
                a = (0.8 - i**2 * 0.1) - j**2 * 0.1
                self.tpoint(px + i, py + j, '#FFFFFF', a)
