class Bingo:
    def __init__(self):
        self.__num_bolas = 0
        self.__bolas_sorteadas = []
        self.__todas_bolas = []

    def iniciar(self, num_bolas):
        self.__num_bolas = num_bolas
        self.__bolas_sorteadas = []
        self.__todas_bolas = []
        for i in range(1, num_bolas + 1):
            self.__todas_bolas.append(i)

    def sortear(self):
        if len(self.__bolas_sorteadas) >= self.__num_bolas:
            return -1
        for bola in self.__todas_bolas:
            if bola not in self.__bolas_sorteadas:
                self.__bolas_sorteadas.append(bola)
                return bola

    def get_sorteados(self):
        return self.__bolas_sorteadas.copy()

    def get_num_bolas(self):
        return self.__num_bolas


class BingoUI:
    def __init__(self):
        self.jogo = None

    def menu(self):
        print("1-Iniciar novo jogo")
        print("2-Sortear número")
        print("3-Ver números sorteados")
        print("4-Sair")
        return int(input("Escolha uma opção: "))

    def iniciar_jogo(self):
        num = int(input("Informe o número de bolas para o jogo: "))
        if num <= 0:
            print("Número inválido. Deve ser maior que zero.")
            return
        self.jogo = Bingo()
        self.jogo.iniciar(num)
        print(f"Jogo iniciado com {num} bolas.")

    def sortear(self):
        if self.jogo == None:
            print("Você precisa iniciar o jogo primeiro!")
            return
        input("Pressione Enter para sortear a próxima bola...")
        numero = self.jogo.sortear()
        if numero == -1:
            print("Todas as bolas já foram sorteadas.")
        else:
            print(f"Número sorteado: {numero}")

    def mostrar_sorteados(self):
        if self.jogo == None:
            print("Você precisa iniciar o jogo primeiro!")
            return
        lista = self.jogo.get_sorteados()
        if lista:
            print("Números sorteados:")
            for num in lista:
                print(num)
        else:
            print("Nenhuma bola foi sorteada ainda.")

    def executar(self):
        opc = 0
        while opc != 4:
            opc = self.menu()
            if opc == 1:
                self.iniciar_jogo()
            elif opc == 2:
                self.sortear()
            elif opc == 3:
                self.mostrar_sorteados()
ui = BingoUI()
ui.executar()
