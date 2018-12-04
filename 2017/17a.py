
step = 344
buffer = [0]
pos = 0

for i in range(2017):
    pos = (pos + step) % len(buffer)
    pos += 1
    buffer.insert(pos, i + 1)
    #print(pos, buffer)

index = buffer.index(2017)
print(buffer[index + 1])