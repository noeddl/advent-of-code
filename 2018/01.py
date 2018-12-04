
path = "inputs/01.txt"

# a
print(sum([int(step) for step in open(path).readlines()]))

# b
def get_freq(steps):
    freq = 0
    freqs = set([freq])

    while True:
        for i in steps:
            freq = freq + i
            if freq in freqs:
                return freq
            else:
                freqs.add(freq)

print(get_freq([int(step) for step in open(path).readlines()]))


# Tests
def test():
    assert get_freq([+1, -2, +3, +1]) == 2
    assert get_freq([+1, -1]) == 0
    assert get_freq([+3, +3, +4, -2, -4]) == 10
    assert get_freq([-6, +3, +8, +5, -6]) == 5
    assert get_freq([+7, +7, -2, -7, -4]) == 14
