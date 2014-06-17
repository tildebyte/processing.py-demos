# Punktiert is a particle engine based and thought as an extension of Karsten
# Schmidt's toxiclibs.physics code.  This library is developed through and for
# an architectural context. Based on my teaching experiences over the past
# couple years. (c) 2012 Daniel Köhler, daniel@lab - eds.org
# here: define a
# string of particles by the equal division between a start and end particle

from punktiert.math import Vec
from punktiert.physics import VPhysics, VParticle
from punktiert.physics import VParticleString, VSpring, BWander
# world object
world = None
pString = None


def setup():
    size(800, 600)
    strokeWeight(10)
    # create world object with bouncing behavior
    global world, pString
    world = VPhysics(width, height)
    world.setfriction(0.01)
    # create two particles and add an arbitrary wander behavior
    # for random movement
    particleA = VParticle(250, height * 0.5)
    particleA.addBehavior(BWander(-1, 1, 1))
    particleB = VParticle(width - 250, height * 0.5)
    particleB.addBehavior(BWander(1, 1, 1))
    # create a ParticleString: input: VPhysics, particleA, particleB,
    #                                 resolution, strength
    pString = VParticleString(world, particleA, particleB, 0.1, 0.0002)
    world.addGroup(pString)


def draw():
    background(255)
    stroke(0)
    world.update()
    for s in world.springs:
        line(s.a.x(), s.a.y(), s.b.x(), s.b.y())

    fill(255)
    noStroke()
    head = pString.getHead()
    tail = pString.getTail()
    ellipse(head.x(), head.y(), 7, 7)
    ellipse(tail.x(), tail.y(), 7, 7)
