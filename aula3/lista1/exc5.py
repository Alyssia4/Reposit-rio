print("Informe o número do mês (1 a 12)")
mes = int(input())

if mes == 1:
    nome = "janeiro"
elif mes == 2:
    nome = "fevereiro"
elif mes == 3:
    nome = "março"
elif mes == 4:
    nome = "abril"
elif mes == 5:
    nome = "maio"
elif mes == 6:
    nome = "junho"
elif mes == 7:
    nome = "julho"
elif mes == 8:
    nome = "agosto"
elif mes == 9:
    nome = "setembro"
elif mes == 10:
    nome = "outubro"
elif mes == 11:
    nome = "novembro"
elif mes == 12:
    nome = "dezembro"
else:
    nome = None

if nome is None:
    print("Mês inválido! Digite um número entre 1 e 12.")
else:
    if mes <= 3:
        trimestre = "primeiro"
    elif mes <= 6:
        trimestre = "segundo"
    elif mes <= 9:
        trimestre = "terceiro"
    else:
        trimestre = "quarto"

print("O mês de", nome, "é do", trimestre, "trimestre do ano")