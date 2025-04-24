seq = [1]
for k in range(1, 10):
    seq.append(seq[-1] + k)
for x in seq:
    print(x, end=" ")