

def get_value(v):
    try:
        v = int(v)
    except:     
        v = registers.get(v, 0)
    return v


#path = 'inputs/18_small.txt'
path = 'inputs/18.txt'

instructions = []

with open(path) as f:
    for line in f:
        instructions.append(line.strip().split())

registers = {}

index = 0
last_freq = 0

while index < len(instructions):
    instr = instructions[index]

    i, x = instr[0], instr[1]

    if i == 'rcv':
        if get_value(x) > 0:
            print(last_freq)
            break
    elif i == 'snd':
        last_freq = get_value(x)
    else:
        y = get_value(instr[2])
        v = registers.get(x, 0)
        #print(i, x, y, v)

        if i == 'jgz' and get_value(x) > 0:
            index += y
            continue
        elif i == 'set':
            v = y
        elif i == 'add':
            v = v + y
        elif i == 'mul':
            v = v * y
        elif i == 'mod':
            v = v % y

        registers[x] = v

    index += 1
    #print(registers)
