
path = 'inputs/05.csv'

offsets = []

with open(path) as f:
    for line in f:
        offsets.append(int(line))

pos = 0
counter = 0

while pos < len(offsets):
    offset = offsets[pos]
    if offset >= 3:
        offsets[pos] = offsets[pos] - 1
    else:    
        offsets[pos] = offsets[pos] + 1
    pos += offset
    counter += 1

print(counter)
