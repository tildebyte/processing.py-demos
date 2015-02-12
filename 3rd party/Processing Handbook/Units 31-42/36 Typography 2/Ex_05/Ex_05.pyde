font = None
s = "VERTIGO"
angle = 0.0


def setup():
    size(800, 800)
    global font
    font = loadFont("Eureka-90.vlw")
    textFont(font, 24)
    fill(0)


def draw():
    background(204)
    global angle
    angle += 0.02
    pushMatrix()
    translate(33, 50)
    scale((cos(angle / 4.0) + 1.2) * 2.0)
    rotate(angle)
    text(s, 0, 0)
    popMatrix()
