class Coordinate:

    letters = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.x) + ", " + str(self.y)

    def __eq__(self, other):
        return self.x == other.x & \
               self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def get_letter(self, x, y, grid):
        letter = grid[y][x]
        if letter == "E":
            return self.letters.index("z")
        return self.letters.index(grid[y][x])

    def get_adjacents(self, grid):
        adjacents = set()
        self_letter_value = self.get_letter(self.x, self.y, grid)
        if self.x != 0:
            if self.get_letter(self.x-1, self.y, grid) <= self_letter_value+1:
                adjacents.add(str(Coordinate(self.x-1, self.y)))
        if self.x != len(grid[0])-1:
            if self.get_letter(self.x+1, self.y, grid) <= self_letter_value+1:
                adjacents.add(str(Coordinate(self.x+1, self.y)))
        if self.y != 0:
            if self.get_letter(self.x, self.y-1, grid) <= self_letter_value+1:
                adjacents.add(str(Coordinate(self.x, self.y-1)))
        if self.y != len(grid)-1:
            if self.get_letter(self.x, self.y+1, grid) <= self_letter_value+1:
                adjacents.add(str(Coordinate(self.x, self.y+1)))
        return adjacents

