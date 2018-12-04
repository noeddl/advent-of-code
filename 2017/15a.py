
class Generator(object):

    def __init__(self, factor, start_value):
        self.factor = factor
        self.previous_value = start_value

    def run(self):
        value = self.previous_value * self.factor % 2147483647
        self.previous_value = value
        return bin(value)

genA = Generator(16807, 703)
genB = Generator(48271, 516)


counter = 0

# Loooooong running!
for i in range(40000000):
    a = genA.run()
    b = genB.run()
    #if i % 100000 == 0:
    #    print(i)

    if a[-16:] == b[-16:]:
        counter += 1

print(counter)
