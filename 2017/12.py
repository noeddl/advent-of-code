

#path = 'inputs/12_small.txt'
path = 'inputs/12.txt'

nodes = {}

with open(path) as f:
    for line in f:
        line = line.strip()
        left, right = line.split(' <-> ')
        targets = right.split(', ')
        nodes[left] = targets

def find_group(n):
    queue = [n]
    group = []

    while queue:
        n = queue.pop()
        group.append(n)
        for t in nodes[n]:
            if t not in queue and t not in group:
                queue.append(t)

    return group

# a
group = find_group('0')
print(len(group))

# b
groups = []
group_map = {}

for n in nodes:
    if not group_map.get(n):
        group = find_group(n)
        for t in group:
            group_map[t] = group
        groups.append(group)

print(len(groups))