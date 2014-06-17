# The PooWahInstrument is intended to be the most drum - like of the instruments.
#     There is an intial burst of noise which subsides into a tone.

# Every instrument must implement the Instrument interface so
# playNote() can call the instrument's methods.
class PooWahInstrument implements Instrument

    # create all variables that must be used throughout the class
    Oscil toneOsc
    ADSR hitDamp, adsr
    Line baseFreq
    Noise pinkNoise
    Summer sum
    IIRFilter lpFilt1
    AudioOutput out

    # only one contstructor for this instrument.    Amplitude, beginning frequency, sustained
    # frequency, and the wave which is the basis for the tone, and the AudioOutput are all
    # specified.
    PooWahInstrument(amp, begFreq, susFreq, Wavetable baseWave, AudioOutput output)
    
        # equate class variables to constructor variables as necessary
        out = output

        # create instances of any UGen objects as necessary
        # this ADSR is for the whole note
        adsr = ADSR(1.0, 0.003, 0.0640, 0.2, 0.050)
        pinkNoise = Noise(0.3, Noise.Tint.PINK)
        # this ADSR is only for the noise burst at the beginning
        hitDamp = ADSR(1.0, 0.003, 0.0640, 0.0, 0.050)
        # the tone is made using the baseWave
        toneOsc = Oscil(begFreq, amp, baseWave)
        # the freq of the tone will slide from the beginning freq to the sustained
        #     freq over 67 msecs.
        baseFreq = Line(0.067, begFreq, susFreq)
        lpFilt1 = LowPassSP(susFreq, out.sampleRate())
        sum = Summer()

        # patch everything together up to the output
        # put a sliding oscillator into the sum
        baseFreq.patch(toneOsc.frequency)
        toneOsc.patch(sum)
        # add in a burst of filtered pink noise
        pinkNoise.patch(hitDamp).patch(lpFilt1).patch(sum)
        # and patch the sum to an ADSR
        sum.patch(adsr)


    # every instrument must have a noteOn() method
    def noteOn(dur):
    
        # patch the adsr all the way to the output
        adsr.patch(out)
        # and turn it on
        adsr.noteOn()
        # also turn on the ADSR for the noise
        hitDamp.noteOn()
        # lines must be "activated"
        baseFreq.activate()


    # every instrument must have a noteOff() method
    def noteOff():
    
        # turn off the hitDamp ADSR.    since the sustain level of this is
        # 0.0, this is not strictly necessary, but it's good practice
        hitDamp.noteOff()
        # turn off adsr, which cause the release to begin
        adsr.noteOff()
        # after the release is over, unpatch from the out
        adsr.unpatchAfterRelease(out)


