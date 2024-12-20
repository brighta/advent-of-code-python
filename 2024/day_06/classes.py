class Point:

    def __init__(self, x, y, facing = 'n'):
        self.x = x
        self.y = y
        self.facing = facing

    def __repr__(self):
        return '({}, {} - {})'.format(self.x, self.y, self.facing)

    def __eq__(self, other):
        return (self.x == other.x) & \
               (self.y == other.y) & \
               (self.facing == other.facing)

    def __hash__(self):
        return hash((self.x, self.y))

    def getLetter(self, grid):
        return grid[self.y][self.x]

    def getCoordinates(self):
        return self.x, self.y

    def move(self, grid):
        nextPoint = self.getNext()
        if nextPoint.x < 0 or nextPoint.x >= len(grid[0]) or nextPoint.y < 0 or nextPoint.y >= len(grid):
            return None
        letter = nextPoint.getLetter(grid)
        if letter in ['.', '^']:
            return nextPoint
        if self.facing == 'n':
            self.facing = 'e'
        elif self.facing == 'e':
            self.facing = 's'
        elif self.facing == 's':
            self.facing = 'w'
        else:
            self.facing = 'n'
        return self.move(grid)

    def getNext(self):
        newX = self.x
        newY = self.y
        if self.facing == 'n':
            newY -= 1
        elif self.facing == 'e':
            newX += 1
        elif self.facing == 's':
            newY += 1
        else:
            newX -= 1
        return Point(newX, newY, self.facing)
