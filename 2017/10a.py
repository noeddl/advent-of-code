

positions = [i for i in range(256)]
#lengths = [3, 4, 1, 5]
lengths = [14, 58, 0, 116, 179, 16, 1, 104, 2, 254, 167, 86, 255, 55, 122, 244]
pos = 0
skip = 0

for l in lengths:
    #print(pos, l, skip)
    j = pos + l
    k = j - len(positions)
    if k < 0:
        k = 0
    #print(j, k)
    span = positions[pos:j] + positions[:k]
    #print(span)
    
    span = span[::-1]
    #print('r', span)
    positions[pos:j] = span[0:(l-k)]
    positions[:k] = span[(l-k):]

    pos += l + skip
    if pos >= len(positions):
        pos = pos - len(positions)

    skip += 1
    #print('-', positions)
    #print('-----')

first, second = positions[0], positions[1]

print(first * second)