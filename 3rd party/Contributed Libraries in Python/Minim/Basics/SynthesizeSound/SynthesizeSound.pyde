add_library('minim')

from ddf.minim import Minim
from ddf.minim.ugens import Waves, Oscil

minim = Minim(this)
out = minim.getLineOut()
wave = Oscil(440, 0.5, Waves.SINE)
wave.patch(out)
waveDrawMult = None


def setup():
    size(512, 200, P3D)
    waveDrawMult = height / 2 - height * 0.49


def draw():
    background(0)
    stroke(255)
    strokeWeight(1)

    # draw the waveform of the output
    for i in range(out.bufferSize() - 1):
        line(i, 50 - out.left.get(i) * 50,
             i + 1, 50 - out.left.get(i + 1) * 50)
        line(i, 150 - out.right.get(i) * 50,
             i + 1, 150 - out.right.get(i + 1) * 50)

    # draw the waveform we are using in the oscillator
    stroke(128, 0, 0)
    strokeWeight(4)
    for i in range(width - 1):
        point(i, waveDrawMult * wave.getWaveform().value(float(i) / width))


def mouseMoved():
    amp = map(mouseY, 0, height, 1, 0)
    wave.setAmplitude(amp)

    freq = map(mouseX, 0, width, 110, 880)
    wave.setFrequency(freq)


def keyPressed():
    if key == '1':
        wave.setWaveform(Waves.SINE)
    elif key == '2':
        wave.setWaveform(Waves.TRIANGLE)
    elif key == '3':
        wave.setWaveform(Waves.SAW)
    elif key == '4':
        wave.setWaveform(Waves.SQUARE)
    elif key == '5':
        wave.setWaveform(Waves.QUARTERPULSE)
    else:
        pass
