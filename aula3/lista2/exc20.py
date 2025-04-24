for i in range(1, 11):
    linha = [str(i)]
    for p in range(2, i+1, 2):
        linha.append(str(p))
    print(" ".join(linha))