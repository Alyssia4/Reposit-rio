import math
print("Digite os coeficientes a, b, e c de uma equação do II grau")

a = int(input("informe o coeficiente a"))
b = int(input("informe o coeficiente b"))
c = int(input("informe o coeficiente c"))

delta = b**2 - 4*a*c

if delta < 0:
    print("Impossível calcular")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print("As raízes são", raiz1, "e", raiz2)