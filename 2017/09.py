
def get_score(s):
    level = 0
    score = 0
    status = 'normal'
    prev_status = 'normal'
    garbage_counter = 0

    for c in s:
        if status == 'normal':
            if c == '{':
                level += 1
            elif c == '}':
                score += level
                level -= 1
            elif c == '<':
                status = 'garbage'
            elif c == '!':
                prev_status = 'normal'
                status = 'negate'
        elif status == 'garbage':
            if c == '>':
                status = 'normal'
            elif c == '!':
                prev_status = 'garbage'
                status = 'negate'
            else:
                garbage_counter += 1
        elif status == 'negate':
            status = prev_status

        #print(c, status, prev_status, level, score)

    return score, garbage_counter


# Tests
assert(get_score('{}') == (1, 0))
assert(get_score('{{{}}}') == (6, 0))
assert(get_score('{{},{}}') == (5, 0))
assert(get_score('{{{},{},{{}}}}') == (16, 0))
assert(get_score('{<a>,<a>,<a>,<a>}') == (1, 4))
assert(get_score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == (9, 8))
assert(get_score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == (9, 0))
assert(get_score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == (3, 17))
assert(get_score('<>') == (0, 0))
assert(get_score('<random characters>') == (0, 17))
assert(get_score('<<<<>') == (0, 3))
assert(get_score('<{!>}>') == (0, 2))


path = 'inputs/09.txt'
s = open(path).read()

score, garbage_counter = get_score(s)

# a
print(score)

# b
print(garbage_counter)



