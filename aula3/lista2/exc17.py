for p in input("Digite uma frase:\n").split():
    v = sum(c in "aeiouAEIOU" for c in p)
    for _ in range(v):
        print(p, end=" ")