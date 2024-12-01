path = "inputs/01.txt"

def load_data(path):
    for step in open(path).readlines():
        (left, right) = step.strip().split("   ")
        yield int(left), int(right)

def iter_sorted_data(path):
    left = []
    right = []

    for (l, r) in load_data(path):
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    for (l, r) in zip(left, right):
        yield l, r

# a
print(sum([max(left, right) - min(left, right) for (left, right) in iter_sorted_data(path)]))

def iter_similarity_scores(path):
    counts = {}

    for (_l, r) in load_data(path):
        counts[r] = counts.get(r, 0) + 1

    for (l, _r) in load_data(path):
        count = counts.get(l, 0)
        yield l * count

# b
print(sum(iter_similarity_scores(path)))
