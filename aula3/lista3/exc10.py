def Palavra(texto, pos):
    count = 0
    palavra = ""
    i = 0
    while i < len(texto):
        if texto[i] != " ":
            start = i
            while i < len(texto) and texto[i] != " ":
                i += 1
            if count == pos:
                palavra = texto[start:i]
                break
            count += 1
        i += 1
    return palavra