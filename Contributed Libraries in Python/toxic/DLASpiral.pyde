from toxi.sim.dla import DLA, DLAEventAdapter, DLAGuideLines, DLAConfiguration
from toxi.geom import Vec3D, Spline3D
# from processing.opengl import

dla = None
listener = None
currScale = 6
isOctreeVisible = True


def setup():
    size(640, 480, P3D)
    # compute spiral key points (every 45 degrees)
    points = []
    r = 20
    theta = -TAU
    while theta < 3 * TAU:
        p = Vec3D.fromXYTheta(theta).scale(r)
        p.set(p.x(), p.y(), theta * 4)
        points.append(p)
        r *= 0.92
        theta += TAU / 8

    # use points to compute a spline and
    # use resulting segments as DLA guidelines
    guides = DLAGuideLines()
    guides.addCurveStrip(Spline3D(points).computeVertices(8))
    # create DLA 3D simulation space 128 units wide (cubic)
    global dla
    dla = DLA(128)
    # use default configuration
    dla.setConfig(DLAConfiguration())
    # add guide lines
    dla.setGuidelines(guides)
    # set leaf size of octree
    dla.getParticleOctree().setMinNodeSize(1)
    # add a listener for simulation events
    global listener
    listener = DLAListener()
    dla.addListener(listener)
    textFont(createFont("SansSerif", 12))


def draw():
    background(255)
    # DLA is a *VERY* slow process so we need to
    # compute a large number of iterations each frame
    dla.update(10000)
    fill(0)
    text("particles: " + dla.getNumParticles().__str__(), 20, 20)
    translate(width / 2, height / 2, 0)
    rotateX(mouseY * 0.01)
    rotateY(mouseX * 0.01)
    scale(currScale)
    # draw growth progress and guide particles
    drawOctree(dla.getParticleOctree(), isOctreeVisible, 0xffff0000)
    drawOctree(dla.getGuideOctree(), False, 0xff0000ff)


# self method recursively paints an entire octree structure
def drawOctree(node, doShowGrid, col):
    if doShowGrid:
        drawBox(node)
    if node.getNumChildren() > 0:
        children = node.getChildren()
        for i in range(8):
            if children[i] != null:
                drawOctree(children[i], doShowGrid, col)
    else:
        points = node.getPoints()
        if points != null:
            stroke(col)
            beginShape(POINTS)
            # numP = points.size()
            for i in range(0, points.size, 10):
                p = Vec3D(points.get(i))
                vertex(p.x, p.y, p.z)
            endShape()


def drawBox(node):
    noFill()
    stroke(0, 24)
    pushMatrix()
    translate(node.x, node.y, node.z)
    box(node.getSize())
    popMatrix()


def keyPressed():
    global isOctreeVisible, currScale
    if key == ' - ':
        currScale -= 0.25
    if key == ' = ':
        currScale += 0.25
    if key == 'o':
        isOctreeVisible = not isOctreeVisible
    if key == 's':
        listener.save()


class DLAListener(DLAEventAdapter):

    # self method will be called when all guide segments
    # have been processed
    def dlaAllSegmentsProcessed(dla):
        println("all done, saving...")
        save()

    def save():
        dla.save(sketchPath("spiral.dla"), False)
