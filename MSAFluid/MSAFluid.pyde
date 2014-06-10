"""

 Demo of the MSAFluid library (www.memo.tv/msafluid_for_processing)
 Move mouse to add dye and forces to the fluid.
 Demonstrates feeding input into the fluid.
 Port to processing.py and Superfast Blur added
 (http://incubator.quasimondo.com/processing/superfast_blur.php)
 by Ben Alkov, 2014.

"""
 # Copyright (c) 2008, 2009, Memo Akten, www.memo.tv
 # *** The Mega Super Awesome Visuals Company ***
 # * All rights reserved.
 # *
 # * Redistribution and use in source and binary forms, with or without
 # * modification, are permitted provided that the following conditions are met:
 # *
 # *     * Redistributions of source code must retain the above copyright
 # *         notice, this list of conditions and the following disclaimer.
 # *     * Redistributions in binary form must reproduce the above copyright
 # *         notice, this list of conditions and the following disclaimer in the
 # *         documentation and / or other materials provided with the distribution.
 # *     * Neither the name of MSA Visuals nor the names of its contributors
 # *         may be used to endorse or promote products derived from this software
 # *         without specific prior written permission.
 # *
 # * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 # * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 # * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 # * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
 # * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 # * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES LOSS
 # * OF USE, DATA, OR PROFITS OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
 # * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
 # * OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 # * OF THE POSSIBILITY OF SUCH DAMAGE.
add_library('MSAFluid')

FLUID_WIDTH = 120
invWidth = 0
invHeight = 0
fluidSolver = None
imgFluid = None
aspectRatio = 0


def setup():
    size(960, 640, P3D)
    invWidth = 1.0 / width
    invHeight = 1.0 / height
    aspectRatio = (width * invHeight) ** 2

    # Create fluid and set options.
    fluidSolver = MSAFluidSolver2D((FLUID_WIDTH),
                                   (FLUID_WIDTH * height / width))
    fluidSolver.enableRGB(True).setFadeSpeed(0.003).setDeltaT(0.5).setVisc(0.0001)

    # Create image to hold fluid picture.
    imgFluid = createImage(fluidSolver.getWidth(),
                           fluidSolver.getHeight(), RGB)


def mouseMoved():
    mouseNormX = mouseX * invWidth
    mouseNormY = mouseY * invHeight
    mouseVelX = (mouseX - pmouseX) * invWidth
    mouseVelY = (mouseY - pmouseY) * invHeight
    addForce(mouseNormX, mouseNormY, mouseVelX, mouseVelY)


def draw():
    fluidSolver.update()
    imgFluid.loadPixels()
    for i in range(fluidSolver.getNumCells()):
        imgFluid.pixels[i] = color(fluidSolver.r[i] * 2,
                                   fluidSolver.g[i] * 2,
                                   fluidSolver.b[i] * 2)
    # imgFluid.pixels = fastBlur(imgFluid, 2)
    imgFluid.updatePixels()
    image(imgFluid, 0, 0, width, height)


# Add force and dye to fluid, and create particles.
def addForce(x, y, dx, dy):

    # Balance the x and y components of speed with the screen aspect ratio.
    speed = dx**2 + (dy**2 * aspectRatio)
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


def fastBlur(image, radius):
    # Super Fast Blur v1.1
    # by Mario Klingemann <http://incubator.quasimondo.com>
    #
    # Tip: Multiple invovations of this filter with a small
    # radius will approximate a gaussian blur quite well.
    pix = image.pixels
    if radius < 1:
        return
    divisor = radius * 2 + 1
    divisors = [i / divisor for i in range(256 * divisor)]
    imgWidth = image.width
    imgHeight = image.height
    widthMinus = imgWidth - 1
    heightMinus = imgHeight - 1
    plane = [i for i in range(imgWidth * imgHeight)]
    redPlane, greenPlane, bluePlane = plane, plane, plane
    vsize = max(imgWidth, imgHeight)
    vmin = [i for i in range(vsize)]
    vmax = vmin
    yWidth, yIndex = 0, 0

    for y in range(imgHeight):
        rsum, gsum, bsum = 0, 0, 0
        for i in range(-radius, radius + 1):
            pixel = pix[yIndex + min(widthMinus, max(i, 0))]
            rsum += (pixel & 0xff0000) >> 16
            gsum += (pixel & 0x00f00) >> 8
            bsum += pixel & 0x0000f
        for x in range(imgWidth):
            redPlane[yIndex] = divisors[rsum]
            greenPlane[yIndex] = divisors[gsum]
            bluePlane[yIndex] = divisors[bsum]
            if y == 0:
                vmin[x] = min(x + radius + 1, widthMinus)
                vmax[x] = max(x - radius, 0)
            pixel1 = pix[yWidth + vmin[x]]
            pixel2 = pix[yWidth + vmax[x]]
            rsum += ((pixel1 & 0xff0000) - (pixel2 & 0xff0000)) >> 16
            gsum += ((pixel1 & 0x00f00) - (pixel2 & 0x00f00)) >> 8
            bsum += (pixel1 & 0x0000f) - (pixel2 & 0x0000f)
            yIndex += 1
        yWidth += imgWidth
    for x in range(imgWidth):
        rsum, gsum, bsum = 0, 0, 0
        yPointer = -radius * imgWidth
        for i in range(-radius, radius + 1):
            yIndex = max(0, yPointer) + x
            rsum += redPlane[yIndex]
            gsum += greenPlane[yIndex]
            bsum += bluePlane[yIndex]
            yPointer += imgWidth
        yIndex = x
        for y in range(imgHeight):
            pix[yIndex] = 0xff000000 | (divisors[rsum] << 16) | (divisors[gsum] << 8) | divisors[bsum]
            if x == 0:
                vmin[y] = min(y + radius + 1, heightMinus) * imgWidth
                vmax[y] = max(y - radius, 0) * imgWidth
            pixel1 = x + vmin[y]
            pixel2 = x + vmax[y]
            rsum += redPlane[pixel1] - redPlane[pixel2]
            gsum += greenPlane[pixel1] - greenPlane[pixel2]
            bsum += bluePlane[pixel1] - bluePlane[pixel2]
            yIndex += imgWidth
    return pix
