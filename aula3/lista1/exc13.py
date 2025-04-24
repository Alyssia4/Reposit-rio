print("Digite dez valores inteiros")

numeros = list(map(int, input().split()))

maior = max(numeros)
menor = min(numeros)

print(f"O maior valor é {maior} e o menor é {menor}")