"""
 Copyright (c) 2008, 2009, Memo Akten, www.memo.tv
** The Mega Super Awesome Visuals Company **
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are met:

         * Redistributions of source code must retain the above copyright
             notice, this list of conditions and the following disclaimer.
         * Redistributions in binary form must reproduce the above copyright
             notice, this list of conditions and the following disclaimer in the
             documentation and / or other materials provided with the distribution.
         * Neither the name of MSA Visuals nor the names of its contributors
             may be used to endorse or promote products derived from this software
             without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
 FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES LOSS
 OF USE, DATA, OR PROFITS OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
 OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
 OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 OF THE POSSIBILITY OF SUCH DAMAGE.

 """

# from javax.media.opengl import
# from java.nio import

def fadeToColor(GL2 gl, r, g, b, speed):
        gl.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
        gl.glColor4(r, g, b, speed)
        gl.glBegin(gl.GL_QUADS)
        gl.glVertex2(0, 0)
        gl.glVertex2(width, 0)
        gl.glVertex2(width, height)
        gl.glVertex2(0, height)
        gl.glEnd()

class ParticleSystem
        FloatBuffer posArray
        FloatBuffer colArray

        static maxParticles = 5000
        curIndex

        Particle[] particles

        ParticleSystem()
                particles = Particle[maxParticles]
                for i = 0 in range( i < maxParticles): # i++
                curIndex = 0

                posArray = ByteBuffer.allocateDirect(maxParticles * 2 * 2).order(ByteOrder.nativeOrder()).asFloatBuffer()# 2 coordinates per point, 2 points per particle (current and previous)
                colArray = ByteBuffer.allocateDirect(maxParticles * 3 * 2).order(ByteOrder.nativeOrder()).asFloatBuffer()

        def updateAndDraw():
                #OPENGL Processing 2.0
                GL2 gl2 = ((PJOGL)beginPGL()).gl.getGL2()

                gl2.glEnable(GL.GL_BLEND)                         # enable blending
                if !drawFluid) fadeToColor(gl2, 0, 0, 0, 0.05:

                gl2.glBlendFunc(gl2.GL_ONE, GL.GL_ONE)    # additive blending (ignore alpha)
                gl2.glEnable(gl2.GL_LINE_SMOOTH)                # make points round
                gl2.glLineWidth(1)

                gl2.glBegin(gl2.GL_LINES)                             # start drawing points
                for i = 0 in range( i < maxParticles): # i++
                        if particles[i].alpha > 0:
                                particles[i].update()
                                particles[i].drawOldSchool(gl2)        # use oldschool renderng


                gl2.glEnd()

                gl2.glDisable(GL.GL_BLEND)
                endPGL()

        def addParticles(x, y, count):
                for i = 0 in range( i < count): # i++

        def addParticle(x, y):
                particles[curIndex].init(x, y)
                curIndex++
                if curIndex >= maxParticles:
 curIndex = 0





