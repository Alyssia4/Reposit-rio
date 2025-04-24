print("Digite quatro números inteiros:")
num1 = int(input("informe o primeiro número:"))
num2 = int(input("informe o segundo número:"))
num3 = int(input("informe o terceiro número:"))
num4 = int(input("informe o quarto número:"))

soma = num1 + num2 + num3 + num4
media = soma/4
print("Média =", int(media))

print("números menores que a media:")
if num1 < media:
    print(num1)
    if num2 < media:
        print(num2)
        if num3 < media:
            print(num3)
            if num4 < media:
                print(num4)
print("Números maiores ou iguais a media:")
if num1 >= media:
    print(num1)
    if num2 >= media:
        print(num2)
        if num3 >= media:
            print(num3)
            if num4 >= media:
                print(num4)