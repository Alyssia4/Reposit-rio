print("Digite quatro números inteiros:")

num1 = int(input("informe o primeiro número:"))
num2 = int(input("informe o segundo número:"))
num3 = int(input("informe o terceiro número:"))
num4 = int(input("informe o quarto número:"))

soma_pares = 0
soma_impares = 0

if num1 % 2 == 0:
    soma_pares += num1
else:
    soma_impares += num1
if num2 % 2 == 0:
    soma_pares += num2
else:
    soma_impares += num2
if num3 % 2 == 0:
    soma_pares += num3
else:
    soma_impares += num3
if num4 % 2 == 0:
    soma_pares += num4
else:
    soma_impares += num4

print("soma_pares =", soma_pares)
print("soma_impares =", soma_impares)