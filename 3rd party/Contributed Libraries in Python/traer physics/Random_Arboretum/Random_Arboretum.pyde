from traer.physics import ParticleSystem
from java.lang.Float import NEGATIVE_INFINITY, POSITIVE_INFINITY

NODE_SIZE = 10
EDGE_LENGTH = 20
EDGE_STRENGTH = 0.2
SPACER_STRENGTH = 1000
physics = None
scaleFactor = 1
centroidX = 0
centroidY = 0


# PROCESSING ##################/
def setup():
    size(400, 400, P3D)
    smooth()
    strokeWeight(2)
    ellipseMode(CENTER)
    global physics
    physics = ParticleSystem(0, 0.1)
    # Runge - Kutta, the default integrator is stable and snappy,
    # but slows down quickly as you add particles.
    # 500 particles = 7 fps on my machine
    # Try self to see how Euler is faster, but borderline unstable.
    # 500 particles = 24 fps on my machine
    #physics.setIntegrator( ParticleSystem.MODIFIED_EULER )
    # Now try self to see make it more damped, but stable.
    #physics.setDrag( 0.2 )
    textFont(loadFont("ArialMT-12.vlw"))
    initialize()


def draw():
    physics.tick()
    if physics.numberOfParticles() > 1:
        updateCentroid()
    background(255)
    fill(0)
    text('{0} PARTICLES\n{1} FPS'.format(physics.numberOfParticles(), frameRate), 10, 20)
    translate(width / 2, height / 2)
    scale(scaleFactor)
    translate(-centroidX, -centroidY)
    drawNetwork()


def drawNetwork():
    # draw vertices
    fill(160)
    noStroke()
    for i in range(physics.numberOfParticles()):
        v = physics.getParticle(i)
        ellipse(v.position().x(), v.position().y(), NODE_SIZE, NODE_SIZE)

    # draw edges
    stroke(0)
    beginShape(LINES)
    for i in range(physics.numberOfSprings()):
        e = physics.getSpring(i)
        a = e.getOneEnd()
        b = e.getTheOtherEnd()
        vertex(a.position().x(), a.position().y())
        vertex(b.position().x(), b.position().y())
    endShape()


def mousePressed():
    addNode()


def mouseDragged():
    addNode()


def keyPressed():
    if key == 'c':
        initialize()
        return

    if key == ' ':
        addNode()
        return


# ME ######################
def updateCentroid():
    xMax = NEGATIVE_INFINITY
    xMin = POSITIVE_INFINITY
    yMin = POSITIVE_INFINITY
    yMax = NEGATIVE_INFINITY
    for i in range(physics.numberOfParticles()):
        p = physics.getParticle(i)
        xMax = max(xMax, p.position().x())
        xMin = min(xMin, p.position().x())
        yMin = min(yMin, p.position().y())
        yMax = max(yMax, p.position().y())

    deltaX = xMax - xMin
    deltaY = yMax - yMin
    global scaleFactor, centroidX, centroidY
    centroidX = xMin + 0.5 * deltaX
    centroidY = yMin + 0.5 * deltaY

    if deltaY > deltaX:
        scaleFactor = height / (deltaY + 50)
    else:
        scaleFactor = width / (deltaX + 50)


def addSpacersToNode(p, r):
    for i in range(physics.numberOfParticles()):
        q = physics.getParticle(i)
        if p != q and p != r:
            physics.makeAttraction(p, q, -SPACER_STRENGTH, 20)


def makeEdgeBetween(a, b):
    physics.makeSpring(a, b, EDGE_STRENGTH, EDGE_STRENGTH, EDGE_LENGTH)


def initialize():
    physics.clear()
    physics.makeParticle()


def addNode():
    p = physics.makeParticle()
    q = physics.getParticle(int(random(0, physics.numberOfParticles() - 1)))
    if q == p:
        q = physics.getParticle(int(random(0, physics.numberOfParticles() - 1)))
    addSpacersToNode(p, q)
    makeEdgeBetween(p, q)
    p.position().set(q.position().x() + random(-1, 1),
                     q.position().y() + random(-1, 1), 0)
