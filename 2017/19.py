
#path = 'inputs/19_small.txt'
path = 'inputs/19.txt'

diagram = {}
pos = None

with open(path) as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c != ' ' and c != '\n':
                diagram[(i, j)] = c
                if i == 0:
                    pos = (i, j)

letters = []
dir = '|'

v_add = 1
v_mul = 1
h_add = 0
h_mul = 1

steps = 0

while True:
    (i, j) = pos
    c = diagram.get(pos)

    if not c:
        break

    #print(pos, c, h_add, h_mul, v_add, v_mul)

    new_pos = (i + (v_add * v_mul), j + (h_add * h_mul))

    if c == '+':
        if v_add == 1:
            h_add = 1
            v_add = 0
            new_pos = (i, j + (h_add * h_mul))
            if not diagram.get(new_pos):
                h_mul = h_mul * -1
                new_pos = (i, j + (h_add * h_mul))
        elif h_add == 1:
            h_add = 0
            v_add = 1
            new_pos = (i + (v_add * v_mul), j)
            if not diagram.get(new_pos):
                v_mul = v_mul * -1
                new_pos = (i + (v_add * v_mul), j)
        
    if c not in ['+', '|', '-']:
        letters.append(c)

    pos = new_pos
    steps += 1

# a
print(''.join(letters))

# b
print(steps)

