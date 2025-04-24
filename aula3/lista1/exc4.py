print("Digite o primeiro horário no formato hh:mm")
entrada1 = input()    

print("Digite o segundo horário no formato hh:mm")
entrada2 = input()      

posicao_do_ponto = entrada1.find(":")  
hora1_str = entrada1[:posicao_do_ponto]  
min1_str  = entrada1[posicao_do_ponto+1:]

posicao_do_ponto = entrada2.find(":")
hora2_str = entrada2[:posicao_do_ponto]
min2_str  = entrada2[posicao_do_ponto+1:]

hora1 = int(hora1_str)
min1  = int(min1_str)
hora2 = int(hora2_str)
min2  = int(min2_str)

soma_horas   = hora1 + hora2
soma_minutos = min1 + min2

if soma_minutos >= 60:
    soma_minutos = soma_minutos - 60
    soma_horas = soma_horas + 1
if soma_horas < 10:
    texto_horas = "0" + str(soma_horas)
else:
    texto_horas = str(soma_horas)

if soma_minutos < 10:
    texto_minutos = "0" + str(soma_minutos)
else:
    texto_minutos = str(soma_minutos)

print("Total de horas = " + texto_horas + ":" + texto_minutos)