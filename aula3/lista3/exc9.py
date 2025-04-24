def Vogais(texto):
    resultado = ""
    for c in texto:
        if c.lower() in "aeiou":
            resultado += c
    return resultado