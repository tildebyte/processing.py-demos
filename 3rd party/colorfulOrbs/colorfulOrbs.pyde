frames = 120
Num = 20
loLimit = 450
hiLimit = 50
diameter = 10
palette = [color(160, 236, 208), color(236, 216, 147),
           color(231, 175, 126), color(183, 131, 118)]


def setup():
    global step, theta
    size(500, 500)
    noStroke()
    edge = 100
    step = (width - 2 * edge) / Num
    theta = 0


def draw():
    global theta
    background('#676E81')
    i = 0
    for color in range(4):
        for x in range(100, 401, step):
            y = map(sin(color * PI / 8 + theta + (TAU / Num * i)),
                    -1, 1, loLimit, hiLimit)
            for depth in range(7):
                fillColor = palette[color % 4]
                fill(fillColor, depth * 30)
                if hiLimit - 100 <= y <= loLimit :
                    scaler = map(y,
                                 loLimit - 100, hiLimit,
                                 1, 2.8 - depth * 0.3)
                ellipse(x, y, diameter * scaler, diameter * scaler)
            fill(fillColor)
            ellipse(x, y, diameter, diameter)
            i += 1
    theta += TAU / frames
