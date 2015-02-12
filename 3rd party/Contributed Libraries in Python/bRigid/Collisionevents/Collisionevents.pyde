# bRigid provides classes for an easier handling of jBullet in Processing. bRigid is thought as a kind of Processing port for the bullet physics simulation library written in C + +.
# This library allows the interaction of rigid bodies in 3D. Geometry/ Shapes are build with Processing PShape Class, for convinient display and export (c) 2013 Daniel Köhler, daniel@lab - eds.org
# here: collisionEvents: counting the number of collisions

from javax.vecmath import Vector3f
# from com.bulletphysics.collision.narrowphase import PersistentManifold
# from com.bulletphysics.dynamics import RigidBody
from peasy import PeasyCam
from bRigid import BBox, BPhysics

cam = None
world = None


def setup():
    size(500, 720, P3D)
    frameRate(45)
    global cam, world
    cam = PeasyCam(this, 600)
    # extends of physics world
    min = Vector3f(-120, -250, -120)
    max = Vector3f(120, 250, 120)
    # create a rigid physics engine with a bounding box
    world = BPhysics(min, max)
    #set gravity
    world.world.setGravity(Vector3f(0, -10, 0))


def draw():
    background(255)
    lights()
    # rotateY(frameCount * 0.01)
    if frameCount % 10 == 0:
        pos = Vector3f(random(30), 200, random(30))
        b = BBox(this, 20, pos, Vector3f(15, 60, 15), True)
        world.addBody(b)

    world.update()

    # check if bodies are intersecting
    collisionBodies = []
    numManifolds = world.world.getDispatcher().getNumManifolds()
    for i in range(numManifolds):
        contactManifold = world.world.getDispatcher().getManifoldByIndexInternal(i)
        numCon = contactManifold.getNumContacts()
        # change and use self number
        if numCon > 0:
            rA = contactManifold.getBody0()
            rB = contactManifold.getBody1()
            collisionBodies.append(rA)
            collisionBodies.append(rB)

    # mark the colliding bodies
    for r in world.rigidBodies:
        rb = r.rigidBody
        if rb in collisionBodies:
            r.display(Vector3f(0, 240, 240))
        else:
            r.display(Vector3f(240, 240, 240))
