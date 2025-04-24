print("Digite três valores inteiros")
valor1 = int(input("informe o primeiro valor:"))
valor2 = int(input("informe o segundo valor:"))
valor3 = int(input("informe o terceiro valor:"))

maior = max(valor1, valor2, valor3)
menor = min(valor1, valor2, valor3)

soma = maior + menor

print("A soma do maior com o menor número é", soma)