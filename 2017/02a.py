import re

path = 'inputs/02.csv'

checksum = 0

with open(path) as f:
    for row in f:
        row = row.strip()
        cols = re.split('\s+', row)
        cols = [int(col) for  col in cols]
        n = max(cols) - min(cols)
        checksum += n

print(checksum)