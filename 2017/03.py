
def new_coord(x_step, y_step):
    (x, y) = coords[-1]
    c = (x + x_step, y + y_step)
    coords.append(c)

def create_coords(rounds):
    sign = 1

    for r in range(1, rounds):
        for i in range(r):
            new_coord(sign * 1, 0)
        for i in range(r):
            new_coord(0, sign * 1)
        sign = sign * -1

    return coords

def lookup_coords(i):
    return coords[i - 1]

def dist(i, j):
    (x_i, y_i) = lookup_coords(i)
    (x_j, y_j) = lookup_coords(j)
    return abs(x_i - x_j) + abs(y_i - y_j)

coords = [(0,0)]
coords = create_coords(1000)

# ----- Part A -----
print(dist(1, 368078))

# ----- Part B -----

def lookup_cell(x, y):
    for i, c in enumerate(coords):
        if c == (x, y):
            return i + 1

def get_neighbours(i):
    (x, y) = lookup_coords(i)
    neighbours = [
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
        (x - 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
    ]

    return [lookup_cell(x, y) for (x, y) in neighbours]

memory = {1:1}

for (x, y) in coords[1:]:
    cell = lookup_cell(x, y)
    sum = 0
    for n in get_neighbours(cell):
        sum += memory.get(n, 0)
    memory[cell] = sum

    if sum > 368078:
        print(sum)
        break


