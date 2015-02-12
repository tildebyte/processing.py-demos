from ball import Ball


NumBalls = 90
Balls = None
framecounter = 0
save = False


def setup():
    global Balls
    size(800, 600, P2D)
    background(10)
    Balls = [Ball(i)
             for i in range(NumBalls)]


def draw():
    noStroke()
    blendMode(BLEND)
    fill(0, 20)
    rect(0, 0, width, height)
    for ball in Balls:
        ball.run(Balls)
    if save:
        if frameCount % 1 == 0 and frameCount < framecounter + (240 * 3):
            saveFrame("frame####.tif")


def mouseReleased():
    background(10)
    setup()


def keyPressed():
    global save, framecounter
    framecounter = frameCount
    save = not save
