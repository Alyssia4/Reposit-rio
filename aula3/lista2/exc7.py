frase = input("Digite uma frase:\n").split()
i = 0
while i < len(frase):
    print(" ".join(frase[i:]))
    i += 1