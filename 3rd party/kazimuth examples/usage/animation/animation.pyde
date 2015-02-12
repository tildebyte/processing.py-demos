balls = [(20, 20, 2.5, 3, 10), (100, 50, -3.5, -3, 15)]


def setup():
    size(500, 500, P3D)
    frameRate(60)
    ellipseMode(CENTER)
    noStroke()


def draw():
    fill(200, 50)
    rect(0, 0, 500, 500)
    fill(0)
    for i in range(len(balls)):
        x, y, dx, dy, r = balls[i]
        x += dx

        if constrain(x, r, 500 - r) != x:
            dx = -dx

        y += dy

        if constrain(y, r, 500 - r) != y:
            dy = -dy

        balls[i] = x, y, dx, dy, r
        ellipse(x, y, r, r)
