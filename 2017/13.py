
def update_state():
    for d, (s, up) in enumerate(state):
        r = scanners[d]
        if r == 0:
            continue
        if up:
            s += 1
            if s == r:
                up = False
        else:
            s -= 1
            if s == 1:
                up = True

        state[d] = (s, up)


#path = 'inputs/13_small.txt'
path = 'inputs/13.txt'

scanners = []

with open(path) as f:
    for line in f:
        line = line.strip()
        d, r = line.split(': ')
        d, r = int(d), int(r)
        while d > len(scanners):
            scanners.append(0)
        scanners.append(r)

state = [(0, True)] * len(scanners)

severity = 0

for pos in range(len(scanners)):
    update_state()
    #print(state)
    (s, _) = state[pos]
    #print(pos, s)
    if s == 1:
        severity += pos * scanners[pos]
        #print(severity)

# a
print(severity)

# b
delay = 0

while True:
    #print('------', delay)
    tid = delay
    success = True

    for r in scanners:
        if r > 0:
            loop_length = (2 * r) - 2
            #print (r, loop_length, tid, tid % loop_length)
            if tid % loop_length == 0:
                success = False
                break
        tid += 1

    #if delay % 1000 == 0:
    #    print(delay)

    if success:
        print(delay)
        break

    delay += 1

