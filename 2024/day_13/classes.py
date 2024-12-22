class Machine:

    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize

    def __repr__(self):
        return '[{}, {} - {}]'.format(self.a, self.b, self.prize)

    def __eq__(self, other):
        return (self.a == other.b) & \
               (self.b == other.b) & \
               (self.prize == other.prize)

    def __hash__(self):
        return hash((self.a, self.b, self.prize))


class Values:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) & \
               (self.y == other.y)

    def __hash__(self):
        return hash((self.x, self.y))