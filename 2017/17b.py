
step = 344
pos = 0
pos1 = 0

# Loooooong running!
for i in range(50000000):
    buffer_length = i + 1
    pos = ((pos + step) % buffer_length) + 1
    if pos == 1:
        pos1 = i + 1

print(pos1)