
def dist(tile):
    return max(tile['x'], tile['y'], tile['z'])

def update(tile, dir):
    (up, down) = dirs[dir]
    tile[up] += 1
    tile[down] -= 1

path = open('inputs/11.txt').read().split(',')

tile = {'x':0, 'y':0, 'z':0}

dirs = {
    'n':  ('y', 'z'),
    'ne': ('x', 'z'),
    'se': ('x', 'y'),
    's':  ('z', 'y'),
    'sw': ('z', 'x'),
    'nw': ('y', 'x')
}

dists = []

for step in path:
    update(tile, step)
    dists.append(dist(tile))

# a
print(dist(tile))

# b
print(max(dists))