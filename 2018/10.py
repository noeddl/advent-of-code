import re


class Grid():

    def __init__(self, path):
        self.lights, self.velocities = self.load(path)
        self.light_set = set(self.lights)
        x_coords = [x for (x, _) in self.lights]
        y_coords = [y for (_, y) in self.lights]
        self.left_edge = min(x_coords)
        self.right_edge = max(x_coords)
        self.upper_edge = min(y_coords)
        self.lower_edge = max(y_coords)

    def load(self, path):
        re_line = re.compile(r"position=<\s*([-]?\d+),\s*([-]?\d+)> velocity=<\s*([-]?\d+),\s*([-]?\d+)>")
        lights = []
        velocities = []
        with open(path) as f:
            for i, line in enumerate(f):
                match = re_line.match(line)
                x, y, x_velocity, y_velocity = [int(i) for i in match.groups()]
                lights.append((x, y))
                velocities.append((x_velocity, y_velocity))
        return lights, velocities

    def update_edges(self):
        x_coords = [x for (x, y) in self.lights]
        y_coords = [y for (x, y) in self.lights]
        self.left_edge = min(x_coords)
        self.right_edge = max(x_coords)
        self.upper_edge = min(y_coords)
        self.lower_edge = max(y_coords)        

    def paint(self):
        s = ""
        for y in range(self.upper_edge, self.lower_edge + 1):
            for x in range(self.left_edge, self.right_edge + 1):
                point = '.'
                if (x, y) in self.light_set:
                    point = '#'
                    if not self.has_neighbor(x, y):
                        point = "!"
                s += point
            s += "\n"
        print(s)

    def update(self, seconds=1):
        lights = []
        for i, (x, y) in enumerate(self.lights):
            (x_velocity, y_velocity) = self.velocities[i]
            x += x_velocity * seconds
            y += y_velocity * seconds
            lights.append((x, y))
        self.lights = lights
        self.light_set = set(lights)
        self.update_edges()

    def has_neighbor(self, x, y):
        for (i, j) in [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]:
            (k, l) = (x + i, y + j)
            if (k, l) in self.light_set:
                return True
        return False

    def is_aligned(self):
        for (x, y) in self.lights:
            if not self.has_neighbor(x, y):
                return False
        return True

    # My own solution that I did not get to work at first because of a sneaky error in the
    # neighbor node list ...
    def find_message(self):
        seconds = 0
        while True:
            if self.is_aligned():
                return seconds
            self.update()
            seconds += 1

    # Another version that I came up with after reading around on Reddit - but in fact I prefer
    # my own solution.
    def find_message2(self):
        seconds = 0
        minimal_box = 1e12
        while True:
            box = (self.right_edge - self.left_edge) * (self.lower_edge - self.upper_edge)
            if box < minimal_box:
                minimal_box = box
            elif box > minimal_box:
                return seconds - 1
            self.update()
            seconds += 1

path = "inputs/10.txt"

grid = Grid(path)
seconds = grid.find_message()

# Version 2:
#grid = Grid(path)
#seconds = grid.find_message2()
#grid = Grid(path)
#grid.update(seconds)

# a
grid.paint()

# b
print(seconds)

# Tests
def test():
    grid = Grid("inputs/10_test.txt")
    seconds = grid.find_message()
    assert seconds == 3
