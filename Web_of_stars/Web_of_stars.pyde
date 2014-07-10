from ball import Ball

NUM_BALLS = 90
Balls = []
framecounter = 0
save = False


def setup():
    size(800, 600, P2D)
    # smooth(2)
    background(10)
    initialize()


def draw():
    noStroke()
    blendMode(BLEND)
    fill(0, 20)
    rect(0, 0, width, height)
    for ball in Balls:
        ball.run(Balls)
    if save:
        if frameCount % 1 == 0 and frameCount < framecounter + (240 * 3):
            saveFrame("image-####.tif")


def mouseReleased():
    background(10)
    initialize()


def initialize():
    Balls = []
    for i in range(NUM_BALLS):
        Balls.append(Ball(i))


def keyPressed():
    framecounter = frameCount
    save = not save
