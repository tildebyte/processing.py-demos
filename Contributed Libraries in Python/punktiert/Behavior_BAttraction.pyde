# Punktiert is a particle engine based and thought as an extension of Karsten
# Schmidt's toxiclibs.physics code. This library is developed through and for
# an architectural context. Based on my teaching experiences over the past
# couple years. (c) 2012 Daniel Köhler, daniel@lab-eds.org

# here: global attractor force connected to mouse position

from punktiert.math import Vec
from punktiert.physics import VPhysics, VParticle
from punktiert.physics import BAttraction, BCollision

# world object
world = None
# attractor
attr = None

# number of particles in the scene
amount = 200


def setup():
    size(800, 600)
    noStroke()

    # set up physics
    global world
    world = VPhysics()
    world.setfriction(0.4)

    # new AttractionForce: (Vec pos, radius, strength)
    global attr
    attr = BAttraction(Vec(width * 0.5, height * 0.5), 400, 0.1)
    world.addBehavior(attr)

    for i in range(amount):
        # val for arbitrary radius
        rad = random(2, 20)
        # vector for position
        pos = Vec(random(rad, width - rad), random(rad, height - rad))
        # create particle (Vec pos, mass, radius)
        particle = VParticle(pos, 4, rad)
        # add Collision Behavior
        particle.addBehavior(BCollision())
        # add particle to world
        world.addParticle(particle)


def draw():
    background(255)
    world.update()
    noFill()
    stroke(200, 0, 0)
    # set pos to mousePosition
    attr.setAttractor(Vec(mouseX, mouseY))
    ellipse(attr.getAttractor().x(), attr.getAttractor().y(),
            attr.getRadius(), attr.getRadius())

    noStroke()
    fill(0, 255)
    for p in world.particles:
        ellipse(p.x(), p.y(), p.getRadius() * 2, p.getRadius() * 2)
