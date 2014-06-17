# Punktiert is a particle engine based and thought as an extension of
# Karsten Schmidt's toxiclibs.physics code.
# This library is developed through and for an architectural context.
# Based on my teaching experiences over the past couple years.
# (c) 2012 Daniel Köhler, daniel@lab-eds.org

# here: seek (part of flocking) function as behavior

from punktiert.math import Vec
from punktiert.physics import VPhysics, VParticle, BCollision, BSeek

# world object
world = None
mouse = None

# number of particles in the scene
amount = 100


def setup():
    size(800, 600)
    smooth()
    fill(0, 255)

    global world, mouse
    world = VPhysics()
    mouse = Vec(width * 0.5, height * 0.5)

    # world.setfriction(.99f)

    for i in range(amount):
        # val for arbitrary radius
        rad = random(2, 20)
        # vector for position
        pos = Vec(random(rad, width - rad), random(rad, height - rad))
        # create particle (Vec pos, mass, radius)
        particle = VParticle(pos, 1, rad)
        # add Collision Behavior
        particle.addBehavior(BCollision())
        particle.addBehavior(BSeek(mouse))
        # add particle to world
        world.addParticle(particle)


def draw():
    background(255)
    world.update()
    mouse.set(mouseX, mouseY)
    for p in world.particles:
        drawRectangle(p)


def drawRectangle(p):
    deform = p.getVelocity().mag()
    # println(p.getPreviousPosition())
    # println(p)
    rad = p.getRadius()
    deform = map(deform, 0, 1.5, rad, 0)
    deform = max(rad * 0.2, deform)

    rotation = p.getVelocity().heading()

    pushMatrix()
    translate(p.x(), p.y())
    rotate(HALF_PI * 0.5 + rotation)
    beginShape()
    vertex(-rad, +rad)
    vertex(deform, deform)
    vertex(rad, -rad)
    vertex(-deform, -deform)
    endShape(CLOSE)
    popMatrix()
