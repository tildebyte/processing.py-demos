halfWidth = None
halfHeight = None


def setup():
    size(512, 512, P3D)
    halfWidth = width / 2.0
    halfHeight = height / 2.0


def draw():
    background(0)

    translate(halfWidth, halfHeight)

    step()
    display()
