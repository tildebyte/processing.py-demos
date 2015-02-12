from traer.physics import ParticleSystem
from peasy import PeasyCam

physics = None
others = None
mouse = None


def setup():
    size(400, 400, P3D)
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(50)
    cam.setMaximumDistance(500)
    # frameRate(24)
    cursor(CROSS)
    sphereDetail(10)
    global physics, others, mouse
    # img = loadImage("fade.png")
    # imageMode(CORNER)
    tint(0, 32)
    physics = ParticleSystem(0, 0.1)
    mouse = physics.makeParticle()
    mouse.makeFixed()
    others = [physics.makeParticle(1.0, random(0, width), random(0, height), random(0, (width + height) / 2)) for i in range(1000)]
    for i in range(100):
        # others[i] = physics.makeParticle(1.0, random(0, width), random(0, height), 0)
        physics.makeAttraction(mouse, others[i], 5000, 50)


def draw():
    noStroke()
    lights()
    mouse.position().set(mouseX, mouseY, 0)
    physics.tick()
    background(255)
    for i in range(len(others)):
        # p = others[i]
        # image(img, p.position().x() - img.width / 2, p.position().y() - img.height / 2)
        # ellipse(others[i].position().x() - 5, others[i].position().y() - 5, 10, 10)
        translate(others[i].position().x() - 5, others[i].position().y() - 5, others[i].position().z() - 5)
        sphere(10)
