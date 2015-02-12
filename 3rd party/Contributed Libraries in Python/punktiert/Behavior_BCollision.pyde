#  Punktiert is a particle engine based and thought as an extension of Karsten
#  Schmidt's toxiclibs.physics code. This library is developed through and for
#  an architectural context. Based on my teaching experiences over the past
#  couple years. (c) 2012 Daniel Köhler, daniel@lab-eds.org

# here: spherical collission detection

from punktiert.math import Vec
from punktiert.physics import VPhysics, VParticle
from punktiert.physics import BAttraction, BCollision

# world object
world = None

# number of particles in the scene
amount = 1500


def setup():
    size(800, 600)
    noStroke()
    fill(0, 255)

    global world
    world = VPhysics(width, height)
    world.setfriction(0.1)

    for i in range(amount):
        # val for arbitrary radius
        rad = 10
        # vector for position
        pos = Vec(random(rad, width - rad), random(rad, height - rad))
        # create particle (Vec pos, mass, radius)
        particle = VParticle(pos, 1, rad)
        # add Collision Behavior
        particle.addBehavior(BCollision())
        # add particle to world
        world.addParticle(particle)


def draw():
    background(255)

    world.update()

    for p in world.particles:
        ellipse(p.x(), p.y(), p.getRadius() * 2, p.getRadius() * 2)

    if mousePressed:
        world.addParticle(VParticle(Vec(mouseX, mouseY), 1,
                          10).addBehavior(BCollision()))
