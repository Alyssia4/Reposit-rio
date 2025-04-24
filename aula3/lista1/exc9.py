print("Digite o horário no formato hh:mm")

hora, minuto = input().split(":")
hora = int(hora)
minuto = int(minuto)

if hora < 0 or hora > 12 or minuto < 0 or minuto > 59:
    print("Hora Inválida")
else:
    angulo_hora = (hora % 12) * 30 + (minuto / 60) * 30
    angulo_minuto = minuto * 6

    angulo = abs(angulo_hora - angulo_minuto)
    
    if angulo > 180:
        angulo = 360 - angulo

print(f"Menor ângulo entre os ponteiros = {int(angulo)} graus")