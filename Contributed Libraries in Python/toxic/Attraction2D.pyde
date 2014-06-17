from toxi.geom import Vec2D, Rect
from toxi.physics2d import VerletPhysics2D, VerletParticle2D
from toxi.physics2d.behaviors import AttractionBehavior, GravityBehavior

NUM_PARTICLES = 750
physics = VerletPhysics2D()
mouseAttractor = None
mousePos = Vec2D()


def setup():
    size(680, 382, P3D)
    # setup physics with 10% drag
    physics.setDrag(0.05)
    physics.setWorldBounds(Rect(0, 0, width, height))
    # the NEW way to add gravity to the simulation, using behaviors
    physics.addBehavior(GravityBehavior(Vec2D(0, 0.15)))


def addParticle():
    p = VerletParticle2D(Vec2D.randomVector().scale(5).addSelf(width / 2, 0))
    physics.addParticle(p)
    # add a negative attraction force field around the particle
    physics.addBehavior(AttractionBehavior(p, 20, -1.2, 0.01))


def draw():
    background(255, 0, 0)
    noStroke()
    fill(255)
    if physics.particles.size() < NUM_PARTICLES:
        addParticle()
    physics.update()
    for p in physics.particles:
        ellipse(p.x(), p.y(), 5, 5)


def mousePressed():
    global mousePos, mouseAttractor
    mousePos = Vec2D(mouseX, mouseY)
    # create a positive attraction force field around the mouse position (radius = 250px)
    mouseAttractor = AttractionBehavior(mousePos, 250, 0.9)
    physics.addBehavior(mouseAttractor)


def mouseDragged():
    # update mouse attraction focal point
    mousePos.set(mouseX, mouseY)


def mouseReleased():
    # remove the mouse attraction when button has been released
    physics.removeBehavior(mouseAttractor)
