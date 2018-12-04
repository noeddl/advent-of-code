from functools import reduce

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

    return positions

def reduce_hash(hash):
    dense_hash = ''
    for i in range(16):
        start = i * 16
        end = start + 16
        block = hash[start:end]
        num = reduce(lambda k, l: k ^ l, block)
        dense_hash += format(num, '02x')
    return dense_hash

input = '14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244'

sparse_hash = knot_hash(input)
dense_hash = reduce_hash(sparse_hash)

print(dense_hash)
