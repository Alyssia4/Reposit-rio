print("Digite quatro valores inteiros")

valor1 = int(input("informe o primeiro valor:"))
valor2 = int(input("informe o segundo valor:"))
valor3 = int(input("informe o terceiro valor:"))
valor4 = int(input("informe o quarto valor:"))

if len({valor1, valor2, valor3, valor4}) < 4:
    print("Erro! Os valores não são diferentes.")
else:
    valores = [valor1, valor2, valor3, valor4]
    valores.sort()

    maior = valores[3]
    menor = valores[0]
    segundo_maior = valores[2]
    segundo_menor = valores[1]

    soma = segundo_maior + segundo_menor

print("Maior valor =", maior)
print("Menor valor =", menor)
print("A soma do segundo maior valor com o segundo menor =", soma)