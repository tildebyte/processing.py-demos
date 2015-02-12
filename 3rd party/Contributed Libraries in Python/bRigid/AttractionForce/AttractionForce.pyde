# bRigid provides classes for an easier handling of jBullet in Processing.
# bRigid is thought as a kind of Processing port for the bullet physics
# simulation library written in C++. This library allows the interaction of
# rigid bodies in 3D. Geometry/ Shapes are build with Processing PShape Class,
# for convinient display and export (c) 2013 Daniel Köhler, daniel@lab-eds.org
# here: basic example (Box) for using rigidShapes

from javax.vecmath import Vector3f
from peasy import PeasyCam
from bRigid import BPhysics, BCompound, BConvexHull
from com.bulletphysics.util import ObjectArrayList

cam = None
world = None
pause = False


def setup():
    size(500, 720, P3D)
    frameRate(45)
    global cam, world
    cam = PeasyCam(this, 600)
    min = Vector3f(-1200, -250, -1200)
    max = Vector3f(1200, 1, 1200)
    world = BPhysics(min, max)
    world.world.setGravity(Vector3f(0, 100, 0))

    # add an attraction force
    # BForceAttraction(fixedPosition, radius, strength)
    # f0 = BForceAttraction(Vector3f(0, 100, 0), 500, 800)
    # world.addBehavior(f0)
    # f1 = BForceAttraction(Vector3f(0, -100, 0), 500, 800)
    # world.addBehavior(f1)
    # create a few Compoundshapes
    for j in range(30):
        bComp = BCompound(this, 1, Vector3f(0, 0, 0), True)
        # add bodies, here convexhulls from random pointlists
        for i in range(10):
            # create a list of arbitrary points around a certain radius
            vertices = ObjectArrayList()
            for k in range(32):
                v = Vector3f(random(-5, 5), random(-5, 5), random(-5, 5))
                vertices.add(v)

            c = BConvexHull(this, 100, vertices, Vector3f(random(10),
                            random(20), random(20)), True)
            bComp = bComp.addCollisionShape(world, c)

        bComp.setPosition(
            random(-50, 50), random(-100, 100), random(-100, 100))
        world.addBody(bComp)


def draw():
    background(255)
    lights()
    # rotateY(frameCount * 0.01)
    if not pause:
        world.update()
    world.display()


def keyPressed():
    global pause
    pause = not pause
