from crawler import Crawler

# TODO:
# - Get Width, Height from image.

Width = 1024
Height = 680
HalfWidth = Width / 2.0
HalfHeight = Height / 2.0
Crawler.HalfWidth = HalfWidth
Crawler.HalfHeight = HalfHeight
NumCrawlers = 30


def rightHanded():
    # Fix flippin' coordinate system.
    # Not the *same* as right-handed, but good enough.
    # `-Z` comes out of the screen.
    rotateX(TAU / 2)  # Positive `Y` up.
    translate(HalfWidth, -HalfHeight, 0)  # Centered.


def update():
    for c in Crawler.instances:
        c.imgColor = img.pixels[int((c.position.y * Width)) + int(c.position.x)]
        c.update()


def setup():
    global img
    size(Width, Height, P3D)
    img = loadImage('_DSC5309.jpg')
    img.loadPixels()
    noStroke()
    background(128)
    colorMode(HSB, 360, 100, 100)
    rightHanded()
    for _ in range(NumCrawlers):
        Crawler()


def draw():
    rightHanded()
    update()
