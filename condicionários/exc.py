import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self._id = id
        self._nome = nome
        self._email = email
        self._fone = fone

    def set_nome(self, nome):
        self._nome = nome

    def set_email(self, email):
        self._email = email

    def set_fone(self, fone):
        self._fone = fone

    def ToString(self):
        return f"id: {self._id}\nnome: {self._nome}\nemail: {self._email}\nfone: {self._fone}"

class ClienteUI:
    def __init__(self):
        self.clientes = {}

    def menu(self):
        while True:
            print("\n--- Menu de Clientes ---")
            print("1 - Inserir cliente")
            print("2 - Listar todos os clientes")
            print("3 - Buscar cliente por ID")
            print("4 - Atualizar cliente")
            print("5 - Excluir cliente")
            print("6 - Abrir clientes do arquivo")
            print("7 - Salvar clientes no arquivo")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.inserir()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.listar_id()
            elif opcao == "4":
                self.atualizar()
            elif opcao == "5":
                self.excluir()
            elif opcao == "6":
                self.abrir()
            elif opcao == "7":
                self.salvar()
            elif opcao == "0":
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida.")

    def inserir(self):
        id = input("ID: ")
        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Fone: ")
        if id in self.clientes:
            print("ID já existe.")
        else:
            cliente = Cliente(id, nome, email, fone)
            self.clientes[id] = cliente
            print("Cliente cadastrado com sucesso.")

    def listar(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in self.clientes.values():
                print(cliente.ToString())

    def listar_id(self):
        id = input("Digite o ID do cliente: ")
        if id in self.clientes:
            print(self.clientes[id].ToString())
        else:
            print("Cliente não encontrado.")

    def atualizar(self):
        id = input("ID do cliente para atualizar: ")
        if id in self.clientes:
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            fone = input("Novo fone: ")
            cliente = self.clientes[id]
            cliente.set_nome(nome)
            cliente.set_email(email)
            cliente.set_fone(fone)
            print("Cliente atualizado com sucesso.")
        else:
            print("Cliente não encontrado.")

    def excluir(self):
        id = input("ID do cliente a excluir: ")
        if id in self.clientes:
            del self.clientes[id]
            print("Cliente removido com sucesso.")
        else:
            print("Cliente não encontrado.")

    def abrir(self):
        arquivo = open("clientes.json", "r")
        dados = json.load(arquivo)
        arquivo.close()

        self.clientes = {}
        for id, cliente_dict in dados.items():
            cliente = Cliente(cliente_dict["_id"], cliente_dict["_nome"], cliente_dict["_email"], cliente_dict["_fone"])
            self.clientes[id] = cliente
        print("Clientes carregados do arquivo.")

    def salvar(self):
        dados = {}
        for id, cliente in self.clientes.items():
            dados[id] = cliente.__dict__

        arquivo = open("clientes.json", "w")
        json.dump(dados, arquivo, indent=4)
        arquivo.close()
        print("Clientes salvos no arquivo.")

if __name__ == "__main__":
    ui = ClienteUI()
    ui.menu()