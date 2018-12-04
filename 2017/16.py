


def spin(progs, num):
    return progs[-num:] + progs[:-num]

def exchange(progs, a, b):
    newprogs = [e for e in progs]
    newprogs[a] = progs[b]
    newprogs[b] = progs[a]
    return newprogs

def partner(progs, a, b):
    i, j = progs.index(a), progs.index(b)
    return exchange(progs, i, j)

def run(progs):
    for mv in moves:
        if mv.startswith('s'):
            progs = spin(progs, int(mv[1:]))
        else:
            a, b = mv[1:].split('/')
            if mv.startswith('x'):
                progs = exchange(progs, int(a), int(b))
            else:
                progs = partner(progs, a, b)
        #print(progs)
    return progs

#programs = ['a', 'b', 'c', 'd', 'e']
programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

#moves =['s1', 'x3/4', 'pe/b']
moves = open('inputs/16.txt').read().split(',')

# a
print(''.join(run(programs)))

# b
states = [programs]
progs = run(programs)

while progs != programs:
    states.append(progs)
    progs = run(progs)
    #print(progs)

i = 1000000000 % len(states)

print(''.join(states[i]))

