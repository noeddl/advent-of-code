import time

class Generator(object):

    def __init__(self, factor, divider, start_value):
        self.factor = factor
        self.divider = divider
        self.previous_value = start_value

    def compute_value(self):
        value = self.previous_value * self.factor % 2147483647
        self.previous_value = value
        return value

    def run(self):
        while True:
            value = self.compute_value()
            #if value % self.divider == 0:
            if value & (self.divider - 1) == 0:
                return value & 0xffff #bin(value)

genA = Generator(16807, 4, 703)
genB = Generator(48271, 8, 516)

start = time.time()

counter = 0

# Loooooong running!
for i in range(5000000):
    a = genA.run()
    b = genB.run()

    if a == b:
        counter += 1

end = time.time()

print(counter)
print('{} seconds'.format(end - start))

