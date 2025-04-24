def Referencia(nome):
    partes = nome.split()
    sobrenome = partes[-1]
    iniciais = ""
    for p in partes[:-1]:
        iniciais += p[0].upper() + "."
    return f"{sobrenome.capitalize()}, {iniciais}"