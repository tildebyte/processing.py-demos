from ddf.minim import Minim
from ddf.minim.ugens import Summer, MoogFilter, Frequency
from Instruments import PlayFlutterSaw, PlayFrequencySweep, PlayResonanceSweep

minim = Minim(this)
mainOut = minim.getLineOut(Minim.STEREO, 256)
sawSummer = Summer()
moog = MoogFilter(3000.0, 0.2)
waveSize = 100.0
notes = ['C2', 'G3', 'E5', 'D6', 'D6', 'C8']
tempo = 130.0
PAN_CENTER = 0.0
PAN_LEFT = -1.0
PAN_RIGHT = 1.0
PAN_L_HALF = -0.5
PAN_R_HALF = 0.5

# Gain in (presumably) dBFS
mainOut.setGain(0)


def setup():
    size(800, 400)
    colorMode(HSB, 360, 1, 1)

    sawSummer.patch(moog).patch(mainOut)
    mainOut.pauseNotes()
    mainOut.setTempo(tempo)

    # PlayFlutterSaw(audiooutput, time, dur, pitch, pan, patchTo)
    PlayFlutterSaw(mainOut, 0.0, 200.0, notes[0], PAN_CENTER, sawSummer)
    PlayFlutterSaw(mainOut, 8.0, 192.0, notes[1], PAN_LEFT, sawSummer)
    PlayFlutterSaw(mainOut, 16.0, 184.0, notes[2], PAN_RIGHT, sawSummer)
    PlayFlutterSaw(mainOut, 32.0, 168.0, notes[3], PAN_R_HALF, sawSummer)
    PlayFlutterSaw(mainOut, 32.01, 167.99, notes[3], PAN_L_HALF, sawSummer)

    # PlayFrequencySweep(audiooutput, time, dur, begin, end, moog)
    PlayFrequencySweep(mainOut, 32.0, 8.0, 3000.0, 10000.0, moog)
    PlayFrequencySweep(mainOut, 44.0, 4.0, 10000.0, 8000.0, moog)
    PlayFrequencySweep(mainOut, 48.0, 8.0, 8000.0, 200.0, moog)
    PlayFrequencySweep(mainOut, 62.0, 4.0, 200.0, 2000.0, moog)
    PlayFrequencySweep(mainOut, 74.0, 12.0, 2000.0, 400.0, moog)

    # PlayResonanceSweep(audiooutput, time, dur, begin, end, moog)
    PlayResonanceSweep(mainOut, 66.0, 4.0, 0.2, 0.8, moog)
    PlayResonanceSweep(mainOut, 74.0, 12.0, 0.8, 0.0, moog)
    PlayResonanceSweep(mainOut, 86.0, 2.0, 0.0, 0.2, moog)
    PlayResonanceSweep(mainOut, 88.0, 2.0, 0.2, 0.0, moog)
    PlayResonanceSweep(mainOut, 90.0, 2.0, 0.0, 0.3, moog)
    PlayResonanceSweep(mainOut, 92.0, 2.0, 0.3, 0.01, moog)
    PlayResonanceSweep(mainOut, 94.0, 3.0, 0.01, 0.9, moog)
    PlayResonanceSweep(mainOut, 122.0, 24.0, 0.9, 0.05, moog)

    PlayFrequencySweep(mainOut, 98.0, 24.0, 400.0, 1000.0, moog)
    PlayFrequencySweep(mainOut, 122.0, 12.0, 1000.0,
                       Frequency.ofPitch(notes[4]).asHz(), moog)

    mainOut.resumeNotes()
#
#
# DRAWING DOWN HERE
#


def hueForSample(sample):
    return map(abs(sample), 0, 1, 120, 450)


def draw():
    # erase the window to black
    lastRez = moog.resonance.getLastValue()
    lastFreq = moog.frequency.getLastValue() / 22100.0
    background(lastFreq * 360.0, 0.5, lastRez)
    # draw using a white stroke
    stroke(255)
    # draw the waveforms
    left = mainOut.left.toArray()
    right = mainOut.right.toArray()
    for i in range(mainOut.bufferSize() - 1):
        # find the x position of each buffer value
        x1 = map(i, 0, mainOut.bufferSize(), 0, width)
        x2 = map(i + 1, 0, mainOut.bufferSize(), 0, width)
        # draw a line from one buffer position to the next for both channels
        stroke(hueForSample(left[i]), 1, 1)
        line(x1, height / 2 - waveSize + left[i] * waveSize,
             x2, height / 2 - waveSize + left[i + 1] * waveSize)
        stroke(hueForSample(right[i]), 1, 1)
        line(x1, height / 2 + waveSize + right[i] * waveSize,
             x2, height / 2 + waveSize + right[i + 1] * waveSize)


def keyPressed():
    # close the AudioOutput
    mainOut.close()
    # stop the minim object
    minim.stop()
