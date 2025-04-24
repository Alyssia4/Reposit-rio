print("Digite uma data no formato dd/mm/aaaa")

data = input()
dia, mes, ano = map(int, data.split("/"))

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", 
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

if mes < 1 or mes > 12 or dia < 1 or dia > 31 or ano < 1900 or ano > 2100:
    print("Data inválida")
else:
    print(f"A data é {dia} de {meses[mes - 1]} de {ano}")