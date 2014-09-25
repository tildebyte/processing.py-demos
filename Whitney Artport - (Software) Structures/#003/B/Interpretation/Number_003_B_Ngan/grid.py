from circle import Circle


class Grid(object):
    '''A grid of values, capable of drawing a vector indicating direction.'''
    def __init__(self, value, margin, gap):
        self.value = value
        self.margin = margin
        self.marginSq = self.margin * 2
        self.gap = gap
        self.fieldSize = (width - self.marginSq) / self.gap
        self.field = [[self.value
                       for _ in range(self.fieldSize)]
                      for _ in range(self.fieldSize)]

    def update(self):
        for i in range(len(self.field)):
            for k in range(len(self.field[0])):
                x, y = self.getLocation(i, k)
                line(x, y,
                     x + 10 * Circle.getFunc('cos', self.field[i][k]),
                     y + 10 * Circle.getFunc('sin', self.field[i][k]))

    def getLocation(self, x, y):
        return x * self.gap + self.margin, y * self.gap + self.margin
