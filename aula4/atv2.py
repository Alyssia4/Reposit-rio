class Viagem:
    def __init__(self, distancia, horas, minutos):
        self.distancia = distancia
        self.horas = horas
        self.minutos = minutos

    def velocidade_media(self):
        tempo_horas = self.horas + self.minutos / 60
        if tempo_horas == 0:
            return 0
        return self.distancia / tempo_horas
    
# testando o código

distancia = float(input("Digite a distância percorrida (em km): "))
horas = int(input("Digite o tempo (horas): "))
minutos = int(input("Digite o tempo (minutos): "))

v = Viagem(distancia, horas, minutos)

print(f"Velocidade média: {v.velocidade_media():.2f} km/h")