from datetime import datetime

class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.__id = id
        self.__data = datetime.strptime(data, '%d/%m/%Y') 
        self.__distancia = float(distancia)
        self.__tempo = float(tempo)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = datetime.strptime(data, '%d/%m/%Y')

    def get_distancia(self):
        return self.__distancia

    def set_distancia(self, distancia):
        self.__distancia = float(distancia)

    def get_tempo(self):
        return self.__tempo

    def set_tempo(self, tempo):
        self.__tempo = float(tempo)

    def __str__(self):
        horas = int(self.__tempo // 60)
        minutos = int(self.__tempo % 60)
        tempo_formatado = f"{horas}h {minutos}min" if horas > 0 else f"{minutos}min"
        data_formatada = self.__data.strftime("%d/%m/%Y")
        return f"[ID: {self.__id}] Data: {data_formatada} | Distância: {self.__distancia:.2f} km | Tempo: {tempo_formatado}"
    
class TreinoUI:
    def __init__(self):
        self.lista = []

    def menu(self):
        while True:
            print("\n--- MENU ---")
            print("1. Inserir novo treino")
            print("2. Listar todos os treinos")
            print("3. Listar treino por ID")
            print("4. Atualizar treino")
            print("5. Excluir treino")
            print("6. Mostrar treino mais rápido")
            print("0. Sair")

            op = input("Escolha uma opção: ")
            if op == '1':
                self.inserir()
            elif op == '2':
                self.listar()
            elif op == '3':
                self.listar_id()
            elif op == '4':
                self.atualizar()
            elif op == '5':
                self.excluir()
            elif op == '6':
                self.mais_rapido()
            elif op == '0':
                break
            else:
                print("Opção inválida!")

    def inserir(self):
        id = input("ID do treino: ")
        data = input("Data (dd/mm/aaaa): ")
        distancia = input("Distância (km): ")
        tempo = input("Tempo (min): ")
        treino = Treino(id, data, distancia, tempo)
        self.lista.append(treino)
        print("Treino inserido com sucesso!")

    def listar(self):
        if not self.lista:
            print("Nenhum treino cadastrado.")
        for treino in self.lista:
            print(treino)

    def listar_id(self):
        id = input("Informe o ID do treino: ")
        for treino in self.lista:
            if treino.get_id() == id:
                print(treino)
                return
        print("Treino não encontrado.")

    def atualizar(self):
        id = input("ID do treino a atualizar: ")
        for treino in self.lista:
            if treino.get_id() == id:
                nova_data = input("Nova data (dd/mm/aaaa): ")
                nova_distancia = input("Nova distância (km): ")
                novo_tempo = input("Novo tempo (min): ")
                treino.set_data(nova_data)
                treino.set_distancia(nova_distancia)
                treino.set_tempo(novo_tempo)
                print("Treino atualizado!")
                return
        print("Treino não encontrado.")

    def excluir(self):
        id = input("ID do treino a excluir: ")
        for treino in self.lista:
            if treino.get_id() == id:
                self.lista.remove(treino)
                print("Treino excluído.")
                return
        print("Treino não encontrado.")

    def mais_rapido(self):
        if not self.lista:
            print("Nenhum treino cadastrado.")
            return

        mais_rapido = self.lista[0]

        for treino in self.lista:
            velocidade_atual = treino.get_distancia() / treino.get_tempo()
            velocidade_mais_rapido = mais_rapido.get_distancia() / mais_rapido.get_tempo()

            if velocidade_atual > velocidade_mais_rapido:
                mais_rapido = treino

        print("Treino mais rápido (maior velocidade média):")
        print(mais_rapido)

if __name__ == "__main__":
    ui = TreinoUI()
    ui.menu()