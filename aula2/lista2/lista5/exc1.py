def maior(x, y):
    if x > y:
        return x
    else:
        return y
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("O maior número é:", maior(num1,num2))