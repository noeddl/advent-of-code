
import copy

def update(banks):
    banks = copy.deepcopy(banks)
    blocks = max(banks)
    pos = banks.index(blocks)
    banks[pos] = 0

    for b in range(blocks):
        pos += 1

        if pos >= len(banks):
            pos = pos - len(banks)

        banks[pos] += 1

    return banks

banks = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]
states = []

while banks not in states:
    states.append(banks)
    banks = update(banks)

# a  
print(len(states))

# b
print(len(states) - states.index(banks))

