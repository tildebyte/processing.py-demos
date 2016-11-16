# main points
#     size = (magnitude|size)
#     color = (spectral color/temperature - this is greatly influenced by size)

# Brightness = f(size)
# Hue = f(size)
# Saturation = fake it to look good
# cloud of random points surrounding stars
#     color ~ distance from main - desturate and redshift
#     redshift = subtract from Hue
# for some total number of other points


# animation ideas:
#    - cycle colors
#    - orbit points around main
#         using gravity "sim", based on size of main points (e.g. followers
#           follow closest, *largest* star)

# TODO:
# - Check for overlap (ugh)

from star import Star
from follower import Follower

Width = 1024
Height = 1024
Star.HalfWidth = Width / 2.0
Star.HalfHeight = Height / 2.0
numStars = 100
numFollowers = 10


def rightHanded():
    # Fix flippin' coordinate system.
    # Not the *same* as right-handed, but good enough.
    # `-Z` comes out of the screen.
    rotateX(TAU / 2)  # Positive `Y` up.
    translate(Width / 2.0, -(Height / 2.0), 0)  # Centered.


def update():
    for s in Star.instances:
        s.update()
    # for f in Follower.instances:
    #     f.update()


def setup():
    size(Width, Height, P3D)
    colorMode(HSB, 360, 100, 100)
    for _ in range(numStars):
        Star()
    # for _ in range(numFollowers):
    #     Follower()
    noStroke()
    ellipseMode(RADIUS)


def draw():
    background(0)
    rightHanded()
    noLoop()
    update()
