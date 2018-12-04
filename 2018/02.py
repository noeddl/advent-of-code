
path = "inputs/02.txt"
boxes = open(path).read().splitlines()

# a
def has_rep(box, n):
    counter = {}
    for c in box:
        counter[c] = counter.get(c, 0) + 1
    return n in counter.values()

def checksum(boxes):
    counter = {}
    for box in boxes:
        if has_rep(box, 2):
            counter[2] = counter.get(2, 0) + 1
        if has_rep(box, 3):
            counter[3] = counter.get(3, 0) + 1
    return counter.get(2, 0) * counter.get(3, 0)

print(checksum(boxes))

# b
def match(a, b):
    for i in range(len(a)):
        a1 = a[:i] + a[i+1:]
        b1 = b[:i] + b[i+1:]
        if a1 == b1:
            return a1

def get_base_box(boxes):
    for a in boxes:
        for b in boxes:
            if a == b:
                continue
            base_box = match(a, b)
            if base_box:
                return base_box 

print(get_base_box(boxes))

# Tests
def test_a():
    test_boxes = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
    assert checksum(test_boxes) == 12

def test_b():
    test_boxes = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
    assert get_base_box(test_boxes) == "fgij"
