from functools import reduce

#---- Recycled from day 10 ----

def knot_hash(input):
    positions = [i for i in range(256)]
    lengths = [ord(c) for c in input] + [17, 31, 73, 47, 23]
    pos = 0
    skip = 0

    for i in range(64):
        for l in lengths:
            j = pos + l
            k = j - len(positions)
            if k < 0:
                k = 0
            span = positions[pos:j] + positions[:k]    
            span = span[::-1]

            positions[pos:j] = span[0:(l-k)]
            positions[:k] = span[(l-k):]

            pos += l + skip
            while pos >= len(positions):
                pos = pos - len(positions)

            skip += 1

    return reduce_hash(positions)

def reduce_hash(hash):
    dense_hash = ''
    for i in range(16):
        start = i * 16
        end = start + 16
        block = hash[start:end]
        num = reduce(lambda k, l: k ^ l, block)
        dense_hash += format(num, '02x')
    return dense_hash

#-------------------------------------------------

#input = 'flqrgnkx'
input = 'xlqgujun'

# a
counter = 0

for i in range(128):
    s = '{}-{}'.format(input, i)
    hash = knot_hash(s)
    row = ''
    for c in hash:
        row += "{0:04b}".format(int(c, 16))
    counter += len(row.replace('0', ''))

print(counter)

# b
def neighbors(i, j):
    return [
        (i, j - 1),
        (i, j + 1),
        (i - 1, j),
        (i + 1, j),
    ]

coords = []

for i in range(128):
    s = '{}-{}'.format(input, i)
    hash = knot_hash(s)
    row = ''
    for c in hash:
        row += "{0:04b}".format(int(c, 16))
    for j, c in enumerate(row):
        if c == '1':
            coords.append((i, j))

grouped = []
counter = 0

for (i, j) in coords:
    if (i, j) in grouped:
        continue
    queue = [(i, j)]
    while queue:
        (i, j) = queue.pop()
        grouped.append((i, j))
        for n in neighbors(i, j):
            if n in coords and not n in grouped:
                queue.append(n)
        #print(queue)
    counter += 1
print(counter)



