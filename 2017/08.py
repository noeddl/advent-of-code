
path = 'inputs/08.txt'

registers = {}
commands = []

with open(path) as f:
    for line in f:
        line = line.strip()
        command = line.split()
        commands.append(command)
        registers[command[0]] = 0

values = []

for c in commands:
    n1, o1, v1, _if, n2, o2, v2 = c
    ops = {'inc': '+=', 'dec': '-='}

    s = 'if {} {} {}:\n'.format(registers[n2], o2, v2)
    s += '    registers["{}"] {} {}'.format(n1, ops[o1], v1)
    #print(s)
    
    exec(s) # Evilness!
    values.append(registers[n1])

# a
print(max(registers.values()))

# b
print(max(values))