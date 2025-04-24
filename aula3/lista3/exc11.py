def Senha(texto):
    senha = ""
    count = 0
    for c in texto + " ":
        if c != " ":
            count += 1
        else:
            if count:
                senha += str(count)
                count = 0
    return senha