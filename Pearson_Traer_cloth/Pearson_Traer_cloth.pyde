from traer.physics import ParticleSystem
from traer.physics import Particle
from traer.physics import Vector3D

angNoise = None
radiusNoise = None
angle = -1.570796
radius = None
physics = None
particles = None
gridSizeX = 125
gridSizeY = 75
gridMidX = (gridSizeX / 2.0)
gridMidY = (gridSizeY / 2.0)
moverX = None
moverY = None

def setup():
    size(500, 300)
    smooth()
    frameRate(24)
    strokeCap(4)
    restart()


def restart():
    background(255)
    angNoise = random(10)
    radiusNoise = random(10)
    physics = ParticleSystem(0, 0.01)
    forceWidth = width / gridSizeX
    forceHeight = height / gridSizeY
    forceWidthHalf = forceWidth / 2.0
    moverX = int(random(gridSizeX))
    moverY = int(random(gridSizeY))
    particles = [[physics.makeParticle(0.2,
                                       x * forceWidth + forceWidthHalf,
                                       y * forceHeight, 0)
                  for x in range(gridSizeX)]
                 for y in range(gridSizeY)]

    for particleList in particles:
        for particle in particleList:
            if particleList.index(particle) == 0:
                physics.makeSpring(particles[particles.index(particleList) - 1][0],
                                   particle,
                                   8, 0.5, forceHeight)
            else:
                physics.makeSpring(particleList[particleList.index(particle) - 1],
                                   particle,
                                   8, 0.5, forceWidth)


def clearBackground():
    fill(255, 15)
    noStroke()
    rect(0, 0, width, height)


def draw():
    physics.tick(0.15)
    if frameCount % 100 == 0:
        moverX = int(random(gridSizeX))
        moverY = int(random(gridSizeY))
    clearBackground()
    stroke(0, 5)
    radiusNoise += 0.02
    radius = (noise(radiusNoise) * 400) + 100
    angNoise += 0.01
    angle += (noise(angNoise) * 10) - 5
    if angle > 360:
        angle -= 360
    if angle < 0:
        angle += 360
    forceWidth = radians(angle)
    forceHeight = 250 + radius * cos(forceWidth)
    forceWidthHalf = 150 + radius * sin(forceWidth)
    currentParticleList = particles[moverY]
    currentParticle = currentParticleList[moverX]
    currentParticle.position().set(forceHeight, forceWidthHalf, 0)
    currentParticle.velocity().set(150, 150, 0)
    noFill()
    for particleList in particles:
        with beginShape():
            for particle in particleList:
                if particle is not currentParticle:
                    curveVertex(particle.position().x(),
                                particle.position().y())
    for index in range(len(particles[0])):  # The length of one list
        with beginShape():
            for particleList in particles:
                if particleList is not currentParticleList:
                    curveVertex(particleList[index].position().x(),
                                particleList[index].position().y())

def mousePressed():
    restart()
