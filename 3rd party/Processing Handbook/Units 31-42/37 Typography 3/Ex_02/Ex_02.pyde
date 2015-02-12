# The word "tickle" jitters when the cursor hovers over
f = None
x = 33  # X - coordinate of text
y = 60  # Y - coordinate of text


def setup():
    size(100, 100)
    global f
    f = loadFont("Eureka-24.vlw")
    textFont(f)
    noStroke()


def draw():
    global x, y
    fill(204, 120)
    rect(0, 0, width, height)
    fill(0)
    # If the cursor is over the text, change the position
    if ((mouseX >= x) and (mouseX <= x + 55) and
        (mouseY >= y - 24) and (mouseY <= y)):
        x += random(-5, 5)
        y += random(-5, 5)

    text("tickle", x, y)
