base = list(range(1, 31))
res = []
for i, v in enumerate(base):
    res.append(v)
    if (i + 1) % 3 == 0:
        res.append(base[i] + base[i-1] + base[i-2])
for x in res:
    print(x, end=" ")