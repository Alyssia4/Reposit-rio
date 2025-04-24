print("Digite uma data no formato dd/mm/aaaa")

data = input()
dia, mes, ano = map(int, data.split("/"))

if ano < 1900 or ano > 2100 or mes < 1 or mes > 12:
    print("A data informada não é válida")
else:
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        dias_por_mes[1] = 29
    
    if dia < 1 or dia > dias_por_mes[mes - 1]:
        print("A data informada não é válida")
    else:
        print("A data informada é válida")