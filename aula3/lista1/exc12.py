print("Digite dois valores inteiros separados por um operador +, -, * ou /")

operacao = input()

if "+" in operacao:
    num1, num2 = operacao.split("+")
    resultado = int(num1) + int(num2)
elif "-" in operacao:
    num1, num2 = operacao.split("-")
    resultado = int(num1) - int(num2)
elif "*" in operacao:
    num1, num2 = operacao.split("*")
    resultado = int(num1) * int(num2)
elif "/" in operacao:
    num1, num2 = operacao.split("/")
    if int(num2) == 0:
        print("Divisão por zero não permitida")
        exit()
    resultado = int(num1) / int(num2)
else:
    print("Operador inválido")
    exit()

print(f"O resultado da operação é {resultado}")