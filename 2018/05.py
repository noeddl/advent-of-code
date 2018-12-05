
def reduce(s):
    i = 0
    length = len(s)
    while i < length - 1:
        c1, c2 = s[i], s[i + 1]
        if abs(ord(c1) - ord(c2)) == 32:
            s = s[:i] + s[i + 2:]
            length = len(s)
            i = i - 1
        else:
            i = i + 1
    return s

def find_shortest(s):
    units = set(s.lower())
    reductions = set()

    for u in units:
        # Get uppercased version of unit.
        c = chr(ord(u) - 32)
        r = s.replace(u, "").replace(c, "")
        r = reduce(r)
        reductions.add(r)

    return min(reductions, key=len)


path = "inputs/05.txt"
polymer = open(path).read()

# a
r = reduce(polymer)
print(len(r))

# b
r = find_shortest(polymer)
print(len(r))


# Tests
def test():
    s = "dabAcCaCBAcCcaDA"
    assert reduce(s) == "dabCBAcaDA"
    assert find_shortest(s) == "daDA"

