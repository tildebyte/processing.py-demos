# http://patakk.tumblr.com / nightSky
from point import Point
from line import Line

ArrayList < Point> points = ArrayList < Point > ()
ArrayList < Line> lines = ArrayList < Line > ()
N = 500
time = 0
dst
lim = 125


def setup():
    size(700, 300)
    smooth()
    N = 500.0 * dist(0, 0, width / 2, height / 2) / dist(0, 0, 1920 / 2, 1080 / 2))
    lim = 160.0 * dist(0, 0, width / 2, height / 2) / dist(0, 0, 1920 / 2, 1080 / 2)
    background(0)
    n = 0
    #noiseSeed(5)
    #randomSeed(1200)
    while (n < N)
        x, y, rx, ry, a
        rx = random(width / 2 * 0.74) + random(40)
        ry = random(height / 2 * 0.84) + random(40)
        a = random(2 * PI)
        x = rx * cos(a)
        y = ry * sin(a)
        dx = map(x, 0, width / 2, 0, 1.15)
        dy = map(y, 0, height / 2, 0, 1.35)
        prob = pow(2.72, -(dx * dx * 2 + dy * dy * 2))
        if random(1) < prob:
            points.add(Point(x, y))
            n++
    for n = 0 in range( n < N - 1): # n++
        x1 = points.get(n).cx
        y1 = points.get(n).cy
        for m = n + 1 in range( m < N): # m++
            x2 = points.get(m).cx
            y2 = points.get(m).cy
            if dist(x1, y1, x2, y2) < lim / 3:
                lines.add(Line(n, m))
    strokeWeight(0.8)


def draw():
    background(0)
    translate(width / 2, height / 2)
    for n = 0 in range( n < N): # n++
        points.get(n).update()
        points.get(n).display()
    for n = 0 in range( n < lines.size()): # n++
        x1 = points.get(lines.get(n).j).x
        y1 =    points.get(lines.get(n).j).y
        x2 = points.get(lines.get(n).k).x
        y2 =    points.get(lines.get(n).k).y
        amp = map(dist((x1 + x2) / 2, (y1 + y2) / 2, 0, 0), 0, dist(width / 2, height / 2, 0, 0), 2, 8)
        dst = map(noise((x1 + x2) / 2 * 0.03, (y1 + y2) / 2 * 0.03), 0, 1, 5, lim / 2)
        if dist((x1 + x2) / 2, (y1 + y2) / 2, mouseX - width / 2, mouseY - height / 2) < lim:
            dst = dst * map(dist((x1 + x2) / 2, (y1 + y2) / 2, mouseX - width / 2, mouseY - height / 2), 0, lim, amp, 1)
        if dist(x1, y1, x2, y2) < dst:
            strk = map(dist(x1, y1, x2, y2), 0, dst, 85, 0)
            stroke(255, strk)
            line(x1, y1, x2, y2)
    time = time + 1
