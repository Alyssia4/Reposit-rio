def MMC(x, y):
    a, b = x, y
    while b:
        a, b = b, a % b
    return x * y // a