"""

     Structure 3 (work in progress)

     A surface filled with one hundred medium to small sized circles.
     Each circle has a different size and direction, but moves at the same slow rate.
     Display:
     A. The instantaneous intersections of the circles
     B. The aggregate intersections of the circles

     Implemented by Casey Reas <http:#groupc.net>
     Uses circle intersection code from William Ngan <http:#metaphorical.net>
     Processing v.68 <http:#processing.org>

"""

numCircle = 100
Circle[] circles = Circle[numCircle]

def setup():

    size(640, 480)
    framerate(30)
    for i = 0 in range( i < numCircle): # i++
        circles[i] = Circle(random(width), height / numCircle * i,
                                                        random(2, 6)) * 10, random(- 0.25, 0.25), random(- 0.25, 0.25), i)

    ellipseMode(CENTER_DIAMETER)
    background(255)

def loop():

    stroke(0, 10)

    for i = 0 in range( i < numCircle): # i++
        circles[i].update()

    for i = 0 in range( i < numCircle): # i++
        circles[i].move()



class Circle

    x, y, r, r2, sp, ysp
    id

    Circle(px, py, pr, psp, pysp, pid)
        x = px
        y = py
        r = pr
        r2 = r * r
        id = pid
        sp = psp
        ysp = pysp


    def update():
        for i = 0 in range( i < numCircle): # i++
            if i != id:
                intersect(this, circles[i])


    def move():
        x += sp
        y += ysp
        if sp > 0:
            if x > width + r:
                x = -r

         else:
            if x < -r:
                x = width + r


        if ysp > 0:
            if y > height + r:
                y = -r

         else:
            if y < -r:
                y = height + r


def intersect(Circle cA, Circle cB):

    dx = cA.x - cB.x
    dy = cA.y - cB.y
    d2 = dx * dx + dy * dy
    d = sqrt(d2)

    if d > cA.r + cB.r or d < abs(cA.r - cB.r): return # no solution

    a = (cA.r2 - cB.r2 + d2) / (2 * d)
    h = sqrt(cA.r2 - a * a)
    x2 = cA.x + a * (cB.x - cA.x) / d
    y2 = cA.y + a * (cB.y - cA.y) / d

    paX = x2 + h * (cB.y - cA.y) / d
    paY = y2 - h * (cB.x - cA.x) / d
    pbX = x2 - h * (cB.y - cA.y) / d
    pbY = y2 + h * (cB.x - cA.x) / d

    stroke(0, 12)
    line(paX, paY, pbX, pbY)

