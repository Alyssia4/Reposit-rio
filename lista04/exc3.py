class Pais:
    def __init__(self, id, nome, populacao, area):
        self.__id = id
        self.__nome = nome
        self.__populacao = populacao
        self.__area = area

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_populacao(self):
        return self.__populacao

    def get_area(self):
        return self.__area

    def set_nome(self, nome):
        self.__nome = nome

    def set_populacao(self, populacao):
        self.__populacao = populacao

    def set_area(self, area):
        self.__area = area

    def densidade(self):
        return self.__populacao / self.__area

    def to_string(self):
        return f"{self.__id} - {self.__nome} - População: {self.__populacao} - Área: {self.__area}"


class PaisUI:
    def __init__(self):
        self.lista = []

    def menu(self):
        print("\n1 - Inserir país")
        print("2 - Listar países")
        print("3 - Atualizar país")
        print("4 - Excluir país")
        print("5 - País mais populoso")
        print("6 - País mais povoado")
        print("7 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao.isdigit():
            return int(opcao)
        else:
            print("Opção inválida.")
            return 0

    def inserir(self):
        print("\n--- Inserir País ---")
        id = int(input("ID do país: "))
        nome = input("Nome do país: ")
        populacao = float(input("População: "))
        area = float(input("Área: "))
        pais = Pais(id, nome, populacao, area)
        self.lista.append(pais)
        print("País cadastrado com sucesso.")

    def listar(self):
        print("\n--- Lista de Países ---")
        if len(self.lista) == 0:
            print("Nenhum país cadastrado.")
        else:
            for pais in self.lista:
                print(pais.to_string())

    def atualizar(self):
        print("\n--- Atualizar País ---")
        id = int(input("Informe o ID do país: "))
        achou = False
        for pais in self.lista:
            if pais.get_id() == id:
                nome = input("Novo nome: ")
                populacao = float(input("Nova população: "))
                area = float(input("Nova área: "))
                pais.set_nome(nome)
                pais.set_populacao(populacao)
                pais.set_area(area)
                print("País atualizado com sucesso.")
                achou = True
        if achou == False:
            print("País não encontrado.")

    def excluir(self):
        print("\n--- Excluir País ---")
        id = int(input("Informe o ID do país: "))
        achou = False
        for pais in self.lista:
            if pais.get_id() == id:
                self.lista.remove(pais)
                print("País excluído com sucesso.")
                achou = True
                break
        if achou == False:
            print("País não encontrado.")

    def mais_populoso(self):
        print("\n--- País Mais Populoso ---")
        if len(self.lista) == 0:
            print("Nenhum país cadastrado.")
        else:
            mais = self.lista[0]
            for pais in self.lista:
                if pais.get_populacao() > mais.get_populacao():
                    mais = pais
            print("País mais populoso:")
            print(mais.to_string())
    def mais_povoado(self):
        print("\n--- País Mais Povoado ---")
        if len(self.lista) == 0:
            print("Nenhum país cadastrado.")
        else:
            mais = self.lista[0]
            for pais in self.lista:
                if pais.densidade() > mais.densidade():
                    mais = pais
            print("País mais povoado:")
            print(mais.to_string())

    def executar(self):
        opc = 0
        while opc != 7:
            opc = self.menu()
            if opc == 1:
                self.inserir()
            elif opc == 2:
                self.listar()
            elif opc == 3:
                self.atualizar()
            elif opc == 4:
                self.excluir()
            elif opc == 5:
                self.mais_populoso()
            elif opc == 6:
                self.mais_povoado()
ui = PaisUI()
ui.executar()