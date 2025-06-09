

class Viagem:
    def __init__(self,destino,distancia,litros):
        self._destino =  destino
        self._distancia = distancia
        self._litros= litros
    def set_destino(self, d):
        if d < 0: raise ValueError()
        self._destino = d 
    def get_destino(self):
        return self._destino
    def set_distancia(self, d):
        if d < 0: raise ValueError()
        self._distancia = d
    def get_distancia(self):
        return self._distancia
    def set_litros(self, l):
        if l <= 0: raise ValueError()
        self._litros = l
    def get_litros(self):
        return self._litros
    def consumo(self):
        return self._distancia / self._litros
    
class UI:
    def menu():
        print("\nMenu:")
        print("1- Calcular consumo:")
        print("2- Fim:")
        opcao = input("Escolha uma opção:")
        return opcao
    def calculo():
        destino = input("Informe o destino:")
        distancia = float(input("Informe a distancia em km:"))
        
        litros = float(input("Informe o combustivel em litros:"))

        viagem = Viagem (destino, distancia, litros)
        print("\n Dados viagem")
        print(f"destino:{viagem.get_destino()}")
        print(f"distancia:{viagem.get_distancia()}")
        print(f"litros:{viagem.get_litros()}")
        consumo = viagem.consumo()
        print(f"consumo medio: {consumo:.2f} km/litros")
    def main():
        while True:
            opcao = UI.menu()
            if opcao == "1":
                UI.calculo()
            elif opcao == "2":
                print("Fim")
                break
            else:
                print("opcao invalida, tente novamente")
UI.main()