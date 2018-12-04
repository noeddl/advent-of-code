import re

def parse(s):
    # Format: #1 @ 1,3: 4x4
    match = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", s)
    id, left, top, width, height = [int(i) for i in match.groups()]
    coords = []
    for j in range(top, top + height):
        for i in range(left, left + width):
           coords.append((i,j))
    return id, coords

def get_overlaps(path):
    counter = {}
    for s in open(path).readlines():
        id, coord_list = parse(s)
        for coords in coord_list:
            counter[coords] = counter.get(coords, 0) + 1
    return sorted([k for (k, v) in counter.items() if v > 1])

def get_noverlap_ids(path):
    ids2coords = {}
    for s in open(path).readlines():
        id, coord_list = parse(s)
        ids2coords[id] = set(coord_list)
    overlaps = set(get_overlaps(path))
    return set([k for (k, v) in ids2coords.items() if len(v & overlaps) == 0])

# a
print(len(get_overlaps("inputs/03.txt")))

# b
print(get_noverlap_ids("inputs/03.txt"))

# Tests
def test():
    assert parse("#3 @ 5,5: 2x2") == (3, [(5,5), (6,5), (5,6), (6,6)])
    assert parse("#123 @ 3,2: 5x4") == (123, [
            (3,2), (4,2), (5,2), (6,2), (7,2),
            (3,3), (4,3), (5,3), (6,3), (7,3),
            (3,4), (4,4), (5,4), (6,4), (7,4),
            (3,5), (4,5), (5,5), (6,5), (7,5),
        ])
    assert get_overlaps("inputs/03_test.txt") == [(3,3), (3,4), (4,3), (4,4)]
    assert get_noverlap_ids("inputs/03_test.txt") == set([3])
