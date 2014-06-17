"""
    A surface filled with one hundred medium to small sized circles. Each
    circle has a different size and direction, but moves at the same slow
    rate.

    Display the instantaneous intersections of the circles

    Implemented by J. Tarbell <http://levitated.net>
    8 April 2004
    Processing v.68

    Port to Processing.py/Processing 2.0 by Ben Alkov 16 June 2014
"""
num = 100
time = 0

# Object array.
# Disc[] discs


# Initialization.
def setup():
    size(500, 500)
    colorMode(RGB, 255)
    ellipseMode(CENTER_RADIUS)
    background(0)

    # Make some discs.
    discs = Disc[num]
    # Arrange in anti - collapsing circle.
    for i in range(numi):
        fx = 0.4 * width * cos(TWO_PI * i / num)
        fy = 0.4 * width * sin(TWO_PI * i / num)
        x = random(width / 2) + fx
        y = random(width / 2) + fy
        r = 5 + random(45)
        bt = 1
        if random(100) < 50:
            bt = -1
        discs[i] = Disc(i, x, y, bt * fx / 1000.0, bt * fy / 1000.0, r)


# Main.
def draw():
    background(0)

    # Move discs.
    for disc in discs:
        disc.move()
        disc.drawSelf()
        disc.render(discs)
        disc.renderPxRiders()


# Methods.
def glowpoint(px, py):
    for i in range(-2, 3):
        for j in range(-2, 3):
            a = (0.8 - i**2 * 0.1) - j**2 * 0.1
            tpoint(px + i, py + j, '#FFFFFF', a)


def tpoint(x1, y1, myc, a):
    # Place translucent point.
    c = get(x1, y1)
    r = red(c) + (red(myc) - red(c)) * a
    g = green(c) + (green(myc) - green(c)) * a
    b = blue(c) + (blue(myc) - blue(c)) * a
    nc = color(r, g, b)
    stroke(nc)
    point(x1, y1)
