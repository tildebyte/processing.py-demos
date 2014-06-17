"""
 * Geometry
 * by Marius Watz.
 *
 * Using sin / cos lookup tables, blends colors, and draws a series of
 * rotating arcs on the screen.
"""

# Trig lookup tables borrowed from Toxi cryptic but effective.
sinLUT = []
cosLUT = []
SINCOS_PRECISION = 1.0
SINCOS_LENGTH= (360.0 / SINCOS_PRECISION)

# System data
dosave = False
num = 0
pt = []
style = []


def setup():
    size(1024, 768, P3D)
    background(255)

    # Fill the tables
    sinLUT = SINCOS_LENGTH]
    cosLUT = SINCOS_LENGTH]
    for i in range(SINCOS_LENGTH):
        sinLUT[i]= Math.sin(i * DEG_TO_RAD * SINCOS_PRECISION)
        cosLUT[i]= Math.cos(i * DEG_TO_RAD * SINCOS_PRECISION)
    num = 150
    pt = [6 * num] # rotx, roty, deg, rad, w, speed
    style = [2 * num] # color, render style

    # Set up arc shapes
    index = 0
    prob
    for i in range(num):
        pt[index++] = random(PI * 2) # Random X axis rotation
        pt[index++] = random(PI * 2) # Random Y axis rotation

        pt[index++] = random(60, 80) # Short to quarter - circle arcs
        if random(100) > 90:
            pt[index] = random(8, 27) * 10
        pt[index++] = random(2, 50) * 5 # Radius. Space them out nicely

        # Width of band
        pt[index++] = random(4, 32)
        if random(100) > 90:
            pt[index] = random(40, 60)
        pt[index++] = radians(random(5, 30)) / 5 # Speed of rotation

        # get colors
        prob = random(100)
        if prob < 30:
            style[i * 2] = colorBlended(random(1), 255, 0, 100, 255, 0, 0, 21)
        elif prob < 70:
            style[i * 2] = colorBlended(random(1), 0, 153, 255, 170, 225, 255, 210)
        elif prob < 90:
            style[i * 2] = colorBlended(random(1), 200, 255, 0, 150, 255, 0, 210)
        else:
            style[i * 2] = color(255, 255, 255, 220)
        if prob < 50:
            style[i * 2] = colorBlended(random(1), 200, 255, 0, 50, 120, 0, 210)
        elif prob < 90:
            style[i * 2] = colorBlended(random(1), 255, 100, 0, 255, 255, 0, 210)
        else:
            style[i * 2] = color(255, 255, 255, 220)

        style[i * 2 + 1] = random(100) % 3


def draw():
    background(0)

    index = 0
    translate(width / 2, height / 2, 0)
    rotateX(PI / 6)
    rotateY(PI / 6)

    for i in range(num):
        with pushMatrix():
            rotateX(pt[index])
            index += 1
            rotateY(pt[index])
            index += 1
            if style[i * 2 + 1]==0:
                stroke(style[i * 2])
                noFill()
                strokeWeight(1)
                arcLine(0, 0, pt[index++], pt[index++], pt[index++])
            elif style[i * 2 +1 ] == 1:
                fill(style[i * 2])
                noStroke()
                arcLineBars(0, 0, pt[index++], pt[index++], pt[index++])
            else:
                fill(style[i * 2])
                noStroke()
                arc(0, 0, pt[index++], pt[index++], pt[index++])

            # increase rotation
            pt[index - 5] += pt[index] / 10
            pt[index - 4] += pt[index] / 20
            index += 1


# Get blend of two colors
def colorBlended(fract, r, g, b, r2, g2, b2, a):
    r2 = (r2 - r)
    g2 = (g2 - g)
    b2 = (b2 - b)
    return color(r + r2 * fract, g + g2 * fract, b + b2 * fract, a)


# Draw arc line
def arcLine(x, y, deg, rad, w):
    a = (min (deg / SINCOS_PRECISION, SINCOS_LENGTH - 1))
    numlines = (w / 2)
    for j in range(numlines):
        with beginShape():
            for i in range(a):
                vertex(cosLUT[i] * rad + x, sinLUT[i] * rad + y)
        rad += 2

# Draw arc line with bars
def arcLineBars(x, y, deg, rad, w):
    a = (min (deg / SINCOS_PRECISION, SINCOS_LENGTH - 1)))
    a /= 4

    beginShape(QUADS)
    for i = 0 in range( i < a): # i += 4
        vertex(cosLUT[i]*(rad) + x, sinLUT[i]*(rad) + y)
        vertex(cosLUT[i]*(rad + w) + x, sinLUT[i]*(rad + w) + y)
        vertex(cosLUT[i + 2]*(rad + w) + x, sinLUT[i + 2]*(rad + w) + y)
        vertex(cosLUT[i + 2]*(rad) + x, sinLUT[i + 2]*(rad) + y)

    endShape()


# Draw solid arc
def arc(x, y, deg, rad, w):
    a = min (deg / SINCOS_PRECISION, SINCOS_LENGTH - 1))
    beginShape(QUAD_STRIP)
    for i = 0 in range( i < a): # i++
        vertex(cosLUT[i]*(rad) + x, sinLUT[i]*(rad) + y)
        vertex(cosLUT[i]*(rad + w) + x, sinLUT[i]*(rad + w) + y)

    endShape()
