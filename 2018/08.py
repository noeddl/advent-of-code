# Recursion ... My brain managed to deal with it quite well for part 1 but part 2
# took me a really long time and I needed to get some inspiration from Reddit ...

def load_numbers(path):
    return [int(i) for i in open(path).read().split()]

def get_meta_sum(numbers, meta_sum=0):
    node_num = numbers.pop(0)
    meta_num = numbers.pop(0)

    for _ in range(node_num):
        meta_sum = get_meta_sum(numbers, meta_sum)

    for _ in range(meta_num):
        meta_sum += numbers.pop(0)

    return meta_sum

def get_root_value(numbers):
    node_num = numbers.pop(0)
    meta_num = numbers.pop(0)

    values = []
    for _ in range(node_num):
        value = get_root_value(numbers)
        values.append(value)

    meta = []
    for _ in range(meta_num):
        value = numbers.pop(0)
        meta.append(value)

    if node_num == 0:
        return sum(meta)

    value = 0
    for i in meta:
        index = i - 1
        if index < node_num:
            value += values[index]

    return value

# a
numbers = load_numbers("inputs/08.txt")
meta_sum = get_meta_sum(numbers)
print(meta_sum)

# b
numbers = load_numbers("inputs/08.txt")
root_value = get_root_value(numbers)
print(root_value)


# Tests:
def test():
    numbers = load_numbers("inputs/08_test.txt")
    assert get_meta_sum(numbers) == 138
    numbers = load_numbers("inputs/08_test.txt")
    assert get_root_value(numbers) == 66
