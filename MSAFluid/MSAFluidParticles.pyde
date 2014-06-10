"""

 Demo of the MSAFluid library (www.memo.tv / msafluid_for_processing)
 Move mouse to add dye and forces to the fluid.
 Click mouse to turn off fluid rendering seeing only particles and their paths.
 Demonstrates feeding input into the fluid and reading data back (to update the particles).
 Also demonstrates using Vertex Arrays for particle rendering.

"""

"""
 Copyright (c) 2008, 2009, Memo Akten, www.memo.tv
 *** The Mega Super Awesome Visuals Company ***
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *         notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *         notice, this list of conditions and the following disclaimer in the
 *         documentation and / or other materials provided with the distribution.
 *     * Neither the name of MSA Visuals nor the names of its contributors
 *         may be used to endorse or promote products derived from this software
 *         without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES LOSS
 * OF USE, DATA, OR PROFITS OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
 * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
 * OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 * """
add_library('MSAFluid')

FLUID_WIDTH = 120
invWidth = 0
invHeight = 0
drawFluid = True
fluidSolver = None
imgFluid = None
aspectRatio2 = 0


def setup():
    size(960, 640, P3D)
    invWidth = 1.0 / width
    invHeight = 1.0 / height
    aspectRatio2 = (width * invHeight) ** 2

    # Create fluid and set options.
    fluidSolver = MSAFluidSolver2D((FLUID_WIDTH), (FLUID_WIDTH * height / width))
    fluidSolver.enableRGB(True).setFadeSpeed(0.003).setDeltaT(0.5).setVisc(0.0001)

    # Create image to hold fluid picture.
    imgFluid = createImage(fluidSolver.getWidth(), fluidSolver.getHeight(), RGB)


def mouseMoved():
    mouseNormX = mouseX * invWidth
    mouseNormY = mouseY * invHeight
    mouseVelX = (mouseX - pmouseX) * invWidth
    mouseVelY = (mouseY - pmouseY) * invHeight
    addForce(mouseNormX, mouseNormY, mouseVelX, mouseVelY)


def draw():
    fluidSolver.update()
    if drawFluid:
        imgFluid.loadPixels()
        for i in range(fluidSolver.getNumCells()):
            d = 2
            imgFluid.pixels[i] = color(fluidSolver.r[i] * d,
                                       fluidSolver.g[i] * d,
                                       fluidSolver.b[i] * d)
        imgFluid.updatePixels()
        image(imgFluid, 0, 0, width, height)


def mousePressed():
    drawFluid = not drawFluid


# Add force and dye to fluid, and create particles.
def addForce(x, y, dx, dy):

    # Balance the x and y components of speed with the screen aspect ratio.
    speed = dx * dx + dy * dy * aspectRatio2
    if speed > 0:
        if x < 0:
            x = 0
        elif x > 1:
            x = 1
        if y < 0:
            y = 0
        elif y > 1:
            y = 1
        colorMult = 5
        velocityMult = 30.0
        index = fluidSolver.getIndexForNormalizedPosition(x, y)
        colorMode(HSB, 360, 1, 1)
        hue = ((x + y) * 180 + frameCount) % 360
        drawColor = color(hue, 1, 1)
        colorMode(RGB, 1)

        fluidSolver.rOld[index] += red(drawColor) * colorMult
        fluidSolver.gOld[index] += green(drawColor) * colorMult
        fluidSolver.bOld[index] += blue(drawColor) * colorMult
        fluidSolver.uOld[index] += dx * velocityMult
        fluidSolver.vOld[index] += dy * velocityMult
