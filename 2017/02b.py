import re

def get_row_result(cols):
    for c1 in cols:
        for c2 in cols:
            if c1 > c2 and c1 % c2 == 0:
                return int(c1/c2)

path = 'inputs/02.csv'

checksum = 0

with open(path) as f:
    for row in f:
        row = row.strip()
        cols = re.split('\s+', row)
        cols = [int(col) for  col in cols]
        n = get_row_result(cols)
        checksum += n

print(checksum)