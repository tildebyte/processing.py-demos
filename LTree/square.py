class Square(object):
    ''' '''
    squares = []

    def __init__(self, radius=1, position=PVector(0, 0),
                 rotation=0):
        Square.squares.append(self)
        self.radius = radius
        self.dia = 2 * self.radius
        self.shape = createShape()
        self.position = position
        if Square.squares.index(self) == 0:
            self.color = color(0)  # black
            self.rotation = rotation
        elif Square.squares.index(self) % 2 != 0:
            self.color = color(255, 0, 0)  # red
            self.rotation = rotation
        elif Square.squares.index(self) % 2 == 0:
            self.color = color(0, 0, 255)  # blue
            self.rotation = rotation
        self.makeSelf()

    def makeSelf(self):
        self.shape.beginShape(QUADS)
        self.shape.fill(self.color)
        self.shape.noStroke()
        self.shape.vertex(0, 0)
        self.shape.vertex(self.dia, 0)
        self.shape.vertex(self.dia, self.dia)
        self.shape.vertex(0, self.dia)
        self.shape.endShape(CLOSE)

    def display(self):
        resetMatrix()
        rotate(radians(self.rotation))
        shape(self.shape, self.position.x, self.position.y, self.dia, self.dia)
