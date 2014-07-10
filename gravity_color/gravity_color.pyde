"""
OpenProcessing Tweak of *@*http:#www.openprocessing.org/sketch/153544*@*
"""

from ball import Ball

balls = []
Sources = None
Ball.Radius = 200


def setup():
    size(600, 600)
    # frameRate(24)
    background(255)
    strokeWeight(0.5)
    noFill()
    numBalls = 500  # The number of lines.
    numSources = 7  # The number of gravity points.

    # Gravity points initialize.
    # Sources = [PVector(width / 2 + Ball.Radius * cos(i * TAU / numSources),
    #                    height / 2 + Ball.Radius * sin(i * TAU / numSources))
    #            for i in range(numSources)]
    Sources = [PVector(int(random(width)),
                       int(random(height)))
               for i in range(numSources)]
    print(Sources)
    # Balls initialize.
    for i in range(numBalls):
        rnd = random(0, TAU)
        balls.append(Ball(PVector(random(3, 15) * cos(rnd),
                                  random(3, 15) * sin(rnd)),
                          Sources))


def draw():
    # fadeToWhite(175)
    for ball in balls:
        ball.reset(Sources)
        ball.move()
        ball.display()
    with pushStyle():
        fill(0)
        for source in Sources:
            ellipse(source.x, source.y, 10, 10)
    # filter(DILATE)


def fadeToWhite(opacity):
    with pushStyle():
        fill(255, opacity)
        noStroke()
        rect(0, 0, width, height)
