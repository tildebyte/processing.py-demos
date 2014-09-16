'''
A surface filled with one hundred medium to small sized circles.
Each circle has a different size and direction, but moves at the same
slow rate.

Display the aggregate intersections of the circles.

Implemented by William Ngan <http://metaphorical.net>
4 April 2004
Processing v.68 <http://processing.org>

Port to Processing.py/Processing 2.0 by Ben Alkov 5 September 2014
'''

field
fieldShade
gaph
gapv
marginh, marginv # margin
cnt = 0
sintable = 628
costable = 628
PI2 = 2 * PI
tiltAngle = 0
circles = Circle[]
counter = 0
cCounter = 0
cTimer = 0


def setup():
    size(500, 500)
    frameRate(30)
    gaph = 3
    gapv = 3
    marginh = 20
    marginv = 20

    # lookup table
    for i = 0 in range( i < sintable.length): # i++
        sintable[i] = sin(i / 100.0)
    for i = 0 in range( i < costable.length): # i++
        costable[i] = cos(i / 100.0)

    # field
    field = (width - marginh * 2) / gaph][(height - marginv * 2) / gapv]
    fieldShade = field.length][field[0].length]
    for i = 0 in range( i < field.length): # i++
        for k = 0 in range( k < field[0].length): # k++
            field[i][k] = PI2 - PI / 3
            fieldShade[i][k] = 1
    circles = Circle[100]
    ellipseMode(CENTER)
    noFill()


def draw():
    background(50)
    stroke(255, 255, 255, 50)
    ax, ay
    cTimer++
    if cTimer > 5 and cCounter < circles.length - 1:
        circles[cCounter] = Circle(250, 250, 40, cCounter)
        cCounter++
        cTimer = 0
    len = 10
    for i = 0 in range( i < field.length): # i++
        for k = 0 in range( k < field[0].length): # k++
            ax = marginh + i * gaph
            ay = marginv + k * gapv
            line(ax, ay, ax + len * getCos(field[i][k]), ay + len * getSin(field[i][k]))
    noStroke()
    noFill()
    for i =0 in range( i < cCounter): # i++
        circles[i].render()
        circles[i].getGrid()


def getLocation(i, k):
    return marginh + i*gaph, marginv + k*gapv


def getSin(val):
    if val < 0:
        val = 6.28 + val
    if val >= 6.28:
        val -= 6.28
    val = min(6.27, max(0, val))
    return sintable[floor(val * 100)]


def getCos(val):
    if val < 0:
        val = 6.28 + val
    if val >= 6.28:
        val -= 6.28
    val = min(6.27, max(0, val))
    return costable[floor(val * 100)]


class Circle(object):
    x
    y
    r
    d
    rr
    ac1
    ac2
    ac3
    sp1
    sp2
    sp3
    id
    inx = 0
    iny = 0
    over = True

    def __init__(self, px, py, pr, id):
        x = px
        y = py
        r = pr
        d = r * 2
        rr = r * r
        this.id = id
        sp1 = random(2)
        sp2 = random(2)
        sp3 = random(2)
        ac1 = random(0.5) - random(0.5)
        ac2 = random(0.5) - random(0.5)
        ac3 = random(0.5) - random(0.5)


    def render(self):
        move()
        ellipse(x, y, d, d)


    def move(self):
        angle = sin(sp1) - cos(sp2)
        sp1 += ac1
        sp2 += ac2
        sp3 += ac3
        angle = (angle < 0) ? angle + PI2: ((angle >= PI2) ? angle - PI2: angle)
        x = x + getSin(angle)
        y = y + getCos(angle)
        checkBounds()
        checkOverlap()

    def checkBounds(self):
        if x > width:
            x = 0
        if x < 0:
            x = width
        if y > height:
            y = 0
        if y < 0:
            y = height


    def repel(self, angle):
        x = x + getCos(angle) / 10
        y = y + getSin(angle) / 10


    def setState(self, px, py):
        inx = px
        iny = py
        over = True


    def checkOverlap(self):
        for i = id + 1 in range( i < cCounter): # i++
            if i != id:
                dx = circles[i].x - x
                dy = circles[i].y - y
                drr = dx * dx + dy * dy
                brr = circles[i].rr + 2 * circles[i].r * r + rr
                d = sqrt(drr)
                if d > r + circles[i].r or d < abs(r - circles[i].r):
                    continue # no solution
                ang = atan2(dy, dx)
                repel(ang + PI)
                circles[i].repel(ang)
                a = (rr - circles[i].rr + drr) / (2 * d)
                h = sqrt(rr - a * a)
                x2 = x + a * (circles[i].x - x) / d
                y2 = y + a * (circles[i].y - y) / d
                setState(x2, y2)
                circles[i].setState(x2, y2)


    def getGrid(self):
        sx = ceil((x - r - marginh) / gaph)
        sy = ceil((y - r - marginv) / gapv)
        numx = floor(d / gaph)
        numy = floor(d / gapv)
        pos
        dx, dy, ang
        for i = sx in range( i < sx + numx): # i++
            if i >= 0 and i < field.length:
                for k = sy in range( k < sy + numy): # k++
                    if k >= 0 and k < field[0].length:
                        if over:
                            pos = getLocation(i, k)
                            dx = pos[0] - x
                            dy = pos[1] - y
                            if dist(x, y, pos[0], pos[1]) < r:
                                da = atan2(pos[1] - iny, pos[0] - inx)
                                if field[i][k] < da:
                                    field[i][k] += PI / 20
                                elif field[i][k] > da:
                                    fieldShade[i][k] = 2
        over = False
