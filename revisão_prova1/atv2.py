print("ler três números inteiros em uma mesma linha")

y, a, m = map(int, input().split())

soma=0
if y % 2 == 0: soma = soma + y
if a % 2 == 0: soma = soma + a
if m % 2 == 0: soma = soma + m
print("soma dos pares:", soma)