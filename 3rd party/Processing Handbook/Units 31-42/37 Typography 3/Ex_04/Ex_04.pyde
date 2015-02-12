# Calculates the size of each letter based on the
# position of the cursor so the letters are larger
# when the cursor is closer

word = "BULGE"
totalOffset = 0
font = None


def setup():
    size(100, 100)
    font = loadFont("Eureka-48.vlw")
    textFont(font)
    textAlign(CENTER)
    fill(0)


def draw():
    background(204)
    global totalOffset
    translate((width - totalOffset) / 2, 0)
    totalOffset = 0
    firstWidth = (width / len(word)) / 4.0
    translate(firstWidth, 0)
    for i in range(len(word)):
        distance = abs(totalOffset - mouseX)
        distance = constrain(distance, 24, 60)
        textSize(84 - distance)
        text(word[i], 0, height - 2)
        letterWidth = textWidth(word[i])
        if i != len(word) - 1:
            totalOffset += letterWidth
            translate(letterWidth, 0)
