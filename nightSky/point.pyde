class Point
    cx, cy, r, d
    rt
    ph
    x, y

    Point(xin, yin)
        cx = xin
        cy = yin
        r = random(5, 30)
        d = map(r, 5, 30, 0.5, 2)
        if random(1) > 0.5:
            rt = True
        else:
            rt = False
        ph = random(360)


    def update():
        if rt:
            x = cx + r * cos(radians(time * d + ph))
        else:
            x = cx + r * cos(radians(- time * d + ph))
        if rt:
            y = cy + r * sin(radians(time * d + ph))
        else:
            y = cy + r * sin(radians(- time * d + ph))


    def display():
        noStroke()
        fill(255)
        ellipse(x, y, d, d)
