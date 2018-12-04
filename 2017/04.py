
def is_valid(phrase):
    counter = {}
    for w in phrase.split():
        counter[w] = counter.get(w, 0) + 1
        if counter[w] > 1:
            return False
    return True

def is_valid2(phrase):
    counter = {}
    for w in phrase.split():
        w = ''.join(sorted(list(w)))
        counter[w] = counter.get(w, 0) + 1
        if counter[w] > 1:
            return False
    return True

path = 'inputs/04.csv'

with open(path) as f:
    counter = 0
    for line in f:
        line = line.strip()
        #if is_valid(line):
        if is_valid2(line):
            counter += 1

print(counter)
