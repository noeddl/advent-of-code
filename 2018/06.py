

class Grid():

    def __init__(self, path):
        # List of target coordinates. The index is used as the ID
        # of the corresponding coordinate.
        self.coords = self.load_coords(path)
        self.size = max([max(x, y) for (x, y) in self.coords]) + 1
        # Map of coordinates to a list of distances to the target coordinate
        # with the same index.
        self.dists = self.collect_distances()

    def load_coords(self, path):
        coords = []

        for line in open(path).read().splitlines():
            i, j = line.split(", ")
            coords.append((int(i), int(j)))

        return coords

    def dist(self, a, b):
        (p1, p2), (q1, q2) = a, b
        return abs(p1 - q1) + abs(p2 - q2)

    # To do: The whole thing could be made faster by collecting and processing
    # the distances in one pass.
    def collect_distances(self):
        dists = {}
        for x in range(self.size):
            for y in range(self.size):
                d = (x, y)
                for c in self.coords:
                    dist = self.dist(c, d)
                    dists.setdefault(d, []).append(dist)
        return dists

    def is_boundary(self, x, y):
        boundaries = set([0, self.size - 1])
        return x in boundaries or y in boundaries

    def get_largest_finite_area(self):
        # List of sizes of the area around each target coordinate.
        areas = [0] * len(self.coords)

        for (x, y) in sorted(self.dists):
            dists = self.dists[(x, y)]
            min_dist = min(dists)
            if len([f for f in dists if f == min_dist]) == 1:
                closest_coord = dists.index(min_dist)
                # Areas that have at least one coordinate at the boundary of the grid
                # are considered infinite.
                if areas[closest_coord] == -1:
                    continue
                if self.is_boundary(x, y):
                    areas[closest_coord] = -1
                else:
                    areas[closest_coord] += 1

        return max(areas)

    def get_area_with_all_distances_less_than(self, limit):
        size = 0
        for (x, y) in sorted(self.dists):
            dists = self.dists[(x, y)]
            if sum(dists) < limit:
                size += 1
        return size


grid = Grid("inputs/06.txt")

# a
print(grid.get_largest_finite_area())

# b
print(grid.get_area_with_all_distances_less_than(10000))


# Tests
def test():
    grid = Grid("inputs/06_test.txt")
    assert grid.get_largest_finite_area() == 17
    assert grid.get_area_with_all_distances_less_than(32) == 16
