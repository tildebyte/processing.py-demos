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
        circles[i] = Circle(random(width), random(height), random(2, 6) * 10,
                                                        random(- 2.0, 2.0), random(- 2.0, 2.0))

    ellipseMode(CENTER_DIAMETER)
    background(255)

def loop():

    background(255)

    for i = 0 in range( i < numCircle): # i++
        circles[i].move()


class Circle

    x, y, r, sp, ysp

    Circle(px, py, pr, psp, pysp)
        x = px
        y = py
        r = pr
        sp = psp
        ysp = pysp


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

        stroke(0)
        noFill()
        ellipse(x, y, r, r)


