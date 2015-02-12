# http://www.rariora.org/galleries/processes/page.php?relay=star.pde
# Built from scratch, but inspired by NodeBox "StarFun"
NumStars = 100  # Set range for number of stars


def setup():
    size(800, 800)
    smooth()
    colorMode(HSB, 360, 255, 255, 255)
    background(0)
    noStroke()
    # stroke(255)


def draw():
    # Move origin to center of window
    translate(width / 2, height / 2)
    # Outer loop resets conditions for each star creation
    for _ in range(NumStars):
        numTris = int(random(2, 75))
        # Turn opacity way down for very cool nebula effect.
        # HSB modified from NodeBox
        fill(random(288, 360), random(100, 255), random(51, 153), random(5, 15))
        # Random scatter. Turn off for starburst
        translate(random(-400, 400), random(-400, 400))
        rotate(random(-3, 3))
        # Parameters for building an isosceles triangle
        tri = tuple(calcTri())
        # Inside loop makes a star from iso triangles
        for _ in range(numTris):
            rotate(TAU / numTris)
            triangle(tri)
    noLoop()

def calcTri():
    # Parameters for building an isosceles triangle
    triBase = random(1, 5)
    triHeight = random(500)
    # Locate near origin to facilitate rotation
    xBase1 = 0 - triBase
    xBase2 = xBase1 + (triBase * 2)
    # average distance between base points
    xTip = (xBase1 + xBase2) / 2
    yBases = 0
    yTip = yBases - triHeight
    return xBase1, yBases, xTip, yTip, xBase2


def mousePressed():
    background(0)
    loop()
