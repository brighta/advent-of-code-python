class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x & \
               self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def move(self, direction):
        if direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1
        elif direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1

    def moveTowards(self, other):
        if other.x == self.x:
            if abs(other.y - self.y) > 1:
                return Coordinate(self.x, self.y + int((other.y - self.y)/2))
            return Coordinate(self.x, self.y)
        if other.y == self.y:
            if abs(other.x - self.x) > 1:
                return Coordinate(self.x + int((other.x - self.x)/2), self.y)
            return Coordinate(self.x, self.y)
        if abs(other.x - self.x) == 1 and abs(other.y - self.y) == 1:
            return Coordinate(self.x, self.y)
        if abs(other.x - self.x) == 1 and abs(other.y - self.y) == 2:
            return Coordinate(self.x + (other.x - self.x), self.y + int((other.y - self.y)/2))
        if abs(other.x - self.x) == 2 and abs(other.y - self.y) == 1:
            return Coordinate(self.x + int((other.x - self.x)/2), self.y + (other.y - self.y))
        if abs(other.x - self.x) == 2 and abs(other.y - self.y) == 2:
            return Coordinate(self.x + int((other.x - self.x)/2), self.y + int((other.y - self.y)/2))
        exit(1)

