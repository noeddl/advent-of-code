

class Prog():

    def __init__(self, p, instructions):
        self.id = p
        self.registers = {'p':p}
        self.queue = []
        self.instructions = instructions
        self.index = 0
        self.other = None
        self.wait = False
        self.send_counter = 0

    def get_value(self, v):
        try:
            v = int(v)
        except:     
            v = self.registers.get(v, 0)
        return v

    def send(self, x):
        self.other.queue.append(self.get_value(x))
        self.send_counter += 1
        #print(self.id, 'snd', self.get_value(x), self.other.queue)

    def receive(self, x):
        #print(self.id, 'rcv', self.queue)
        if not self.queue:
            self.wait = True
            return
        v = self.queue.pop(0)
        self.registers[x] = v
        self.wait = False

    def do(self, i, x, y):
        v = self.registers.get(x, 0)
        #print(self.id, i, x, y, v)

        if i == 'set':
            v = y
        elif i == 'add':
            v = v + y
        elif i == 'mul':
            v = v * y
        elif i == 'mod':
            v = v % y

        self.registers[x] = v        

    def terminated(self):
        return self.index >= len(self.instructions)

    def run(self):
        #print(self.index)
        instr = self.instructions[self.index]
        i, x = instr[0], instr[1]

        if i == 'snd':
            self.send(x)
        elif i == 'rcv':
            self.receive(x)
            if self.wait:
                return
        else:
            y = self.get_value(instr[2])
            if i == 'jgz':
                if self.get_value(x) > 0:
                    #print(self.id, 'jgz', y)
                    self.index += y
                    return
            else:
                self.do(i, x, y)

        self.index += 1


#path = 'inputs/18_small.txt'
path = 'inputs/18.txt'

instructions = []

with open(path) as f:
    for line in f:
        instructions.append(line.strip().split())


prog1 = Prog(0, instructions)
prog2 = Prog(1, instructions)

prog1.other = prog2
prog2.other = prog1

i = 0

while (not prog1.terminated()) and (not prog2.terminated()):
    #if not prog1.terminated():
    prog1.run()
    #if not prog2.terminated():
    prog2.run()

    if prog1.wait and prog2.wait:
        break

    i += 1


print(prog1.send_counter)
print(prog2.send_counter)
