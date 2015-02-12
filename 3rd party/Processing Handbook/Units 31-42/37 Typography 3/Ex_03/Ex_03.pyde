# The horizontal position of the mouse determines the
# rotation angle. The angle accumulates with each letter
# drawn to make the typography curve.

letters = "Flexibility"
f = None


def setup():
    size(100, 100)
    global f, letters
    f = loadFont("Eureka-24.vlw")
    textFont(f)
    fill(0)


def draw():
    background(204)
    pushMatrix()
    translate(0, 33)
    for i in range(len(letters)):
        angle = map(mouseX, 0, width, 0, PI / 8)
        rotate(angle)
        text(letters[i], 0, 0)
        # Offset by the width of the current letter
        translate(textWidth(letters[i]), 0)
    popMatrix()
