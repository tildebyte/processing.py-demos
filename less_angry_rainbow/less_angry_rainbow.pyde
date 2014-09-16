img = loadImage('Less-Angry_Rainbow.png')
img.loadPixels()
for pixelColor in img.pixels:
    println('#{0},'.format(hex(pixelColor, 6)))
