from square import Square


baseRadius = 75.0
angleDelta = 5.08
radiusDelta = 1.618
levels = 4


def setup():
    size(512, 512, P2D)
    global halfWidth, halfHeight, baseSquare, baseLocation
    noLoop()
    rectMode(CENTER)
    shapeMode(CENTER)
    halfWidth = width / 2.0
    halfHeight = height / 2.0
    baseLocation = PVector(halfWidth, height - baseRadius)
    baseSquare = Square(baseRadius, position=baseLocation)
    baseSquare.display()


# base = Square.squares[0]
# odd indices are RH
# even indices are LH
def draw():
    # Append two squares to the list each time through the loop
    for i in range(1, levels):
        Square(baseRadius / (radiusDelta * i),
               PVector(Square.squares[i - 1].position.x,
                       Square.squares[i - 1].position.y
                       - Square.squares[i - 1].radius),
               angleDelta * i)
        Square(baseRadius / (radiusDelta * i),
               PVector(Square.squares[i - 1].position.x,
                       Square.squares[i - 1].position.y
                       - Square.squares[i - 1].radius),
               angleDelta * i)
    for s in Square.squares:
        print('Index: {0}, rotation: {1}'
              .format(Square.squares.index(s), s.rotation))
        s.display()
