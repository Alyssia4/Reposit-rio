print("Digite três valores:")

valor1 = int(input("informe o valor:"))
valor2 = int(input("informe o valor:"))
valor3 = int(input("informe o valor:"))

if valor1 + valor2 > valor3 and valor1 + valor3 > valor2 and valor2 + valor3 > valor1:
    if valor1 == valor2 == valor3:
        print("Esses valores formam um triângulo equilátero")
    elif valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
        print("Esses valores formam um triângulo isósceles")
    else:
        print("Esses valores formam um triângulo escaleno")
else:
    print("Esses valores não formam um triângulo")
