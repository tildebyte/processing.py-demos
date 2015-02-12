from ddf.minim.ugens import Frequency, Line, Oscil
from ddf.minim.ugens import Instrument, Waves, Pan


class FlutterSaw(Instrument):
    def __init__(self, freq, panning, patchTo):
        self.saw = Oscil(freq, 1.0, Waves.SAW)
        self.ampMod = Oscil(2.0, 0.5, Waves.SINE)
        self.pan = Pan(panning)
        self.out = patchTo

    def noteOn(self, dur):
        ampModFreqLine = Line(dur * 0.9, 0.5, Frequency.ofPitch("C3").asHz())
        ampModFreqLine.patch(self.ampMod.frequency).patch(self.saw.amplitude)
        ampModFreqLine.activate()
        self.saw.patch(self.pan).patch(self.out)

    def noteOff(self):
        self.pan.unpatch(self.out)


class FilterFrequency(Instrument):
    def __init__(self, begin, end, moog):
        self.filterFreqLine = Line()
        self.begin = begin
        self.end = end
        self.moog = moog

    def noteOn(self, dur):
        self.filterFreqLine = Line(dur, self.begin, self.end)
        self.filterFreqLine.activate()
        self.filterFreqLine.patch(self.moog.frequency)

    def noteOff(self):
        self.filterFreqLine.unpatch(self.moog)


class FilterResonance(Instrument):
    def __init__(self, begin, end, moog):
        self.filterRezLine = Line()
        self.begin = begin
        self.end = end
        self.moog = moog

    def noteOn(self, dur):
        self.filterRezLine = Line(dur, self.begin, self.end)
        self.filterRezLine.activate()
        self.filterRezLine.patch(self.moog.resonance)

    def noteOff(self):
        self.filterRezLine.unpatch(self.moog)


def PlayFlutterSaw(audiooutput, time, dur, pitch, pan, patchTo):
    audiooutput.playNote(time, dur,
                         FlutterSaw(Frequency.ofPitch(pitch).asHz(),
                                    pan, patchTo))


def PlayFrequencySweep(audiooutput, time, dur, begin, end, moog):
    audiooutput.playNote(time, dur, FilterFrequency(begin, end, moog))


def PlayResonanceSweep(audiooutput, time, dur, begin, end, moog):
    audiooutput.playNote(time, dur, FilterResonance(begin, end, moog))
