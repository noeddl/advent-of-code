
def get_scanners(path):
    scanners = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            d, r = line.split(': ')
            d, r = int(d), int(r)
            while d > len(scanners):
                scanners.append(0)
            scanners.append(r)
    return scanners

def travel(tid, stop_early=False):
    severity = -1
    for d, r in enumerate(scanners):
        if r > 0:
            loop_length = (2 * r) - 2
            if tid % loop_length == 0:
                if stop_early:
                    return
                if severity == -1:
                    severity = 0
                severity += d * r
        tid += 1
    return severity

#path = 'inputs/13_small.txt'
path = 'inputs/13.txt'

scanners = get_scanners(path)

# a
print(travel(0))

# b
delay = 0
while True:
    severity = travel(delay, True)
    if severity == -1:
        print(delay)
        break
    delay += 1
