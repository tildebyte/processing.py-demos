'''A sketch inspired by (a radical misinterpretation of) the math from the
JS1K segment of Steven Wittens' "Making Things With Maths" video. Really,
everything is mine except the math in `segment.py`. See also
http://acko.net/blog/js1k-demo-the-making-of

Implemented in Processing.py/Processing 2.1 by Ben Alkov 11-16 Sept 2014.
'''
from tentacle import Tentacle


def settings():
    fullScreen(OPENGL)


Colors = [[color(121, 53, 31),  # rgb(121, 53, 31)  reds
           color(214, 133, 106)],  # rgb(214, 133, 106)
          [color(63, 79, 8),  # rgb(63, 79, 8)  greens
           color(146, 161, 88)],  # rgb(146, 161, 88)
          [color(62, 74, 89),  # rgb(62, 74, 89)  blues
           color(142, 155, 172)]  # rgb(142, 155, 172)
         ]
NumTentacles = 9

def rotateCoords():
    # Fix flippin' coordinate system.
    # Not the *same* as right-handed, but good enough.
    # `-z` comes out of the screen.
    rotateX(PI)  # y up.
    translate(540, -540, 0)  # Centered.


def fade(opacity):
    # Encapsulate alpha blend.
    # `opacity` < 255 for trails,
    # else no trails.
    if opacity == 255:
        background(0)
    else:
        with pushMatrix():
            fill(0, opacity)
            noStroke()
            translate(0, 0, 10)
            rect(0, 0, 2 * width, 2 * height)

def setup():
    global Tentacles
    background(0)
    frameRate(24)
    rectMode(RADIUS)
    Tentacles = [Tentacle(i, Colors[i % 3])
                 for i in range(NumTentacles)]

def draw():
    # global time
    rotateCoords()
    fade(255)
    # The animation is *much* too fast using `frameCount` on its own.
    time = frameCount * 0.01
    for t in Tentacles:
        # I got weird artifacts with `frameCount` < 5.
        if time < 0.05:
            pass
        t.update(time)
    # saveFrame("frames/screen-######.tif")
