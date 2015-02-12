add_library('minim')

minim = Minim(this)

def setup():
    size(500, 200)
    player = minim.loadFile("chord.wav")
    player.play()

def draw():
    pass
