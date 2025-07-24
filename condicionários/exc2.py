import json 
from datetime import datetime

class Contato:
    def __init__(self, id, nome, email, telefone, nascimento):
        self._id = id
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._nascimento =datetime.strptime(nascimento, '%d/%m/%Y')

    def set_nome(self, nome):
        self._nome = nome

    def set_email(self, email):
        self._email = email

    def set_telefone(self, telefone):
        self._telefone = telefone

    def set_nascimento(self, nascimento):
        self._nascimento = nascimento

    def get_nome(self):
        return self._nome

    def get_nascimento(self):
        return self._nascimento

    def ToString(self):
        return f"id: {self._id}\nnome: {self._nome}\nemail: {self._email}\ntelefone: {self._telefone}\nnascimento: {self._nascimento}\n"

class ContatoUI:
    def __init__(self):
        self.contatos = {}

    def menu(self):
        while True:
            print("\n--- MENU AGENDA ---")
            print("1 - Inserir contato")
            print("2 - Listar todos")
            print("3 - Buscar por ID")
            print("4 - Atualizar contato")
            print("5 - Excluir contato")
            print("6 - Pesquisar por nome (iniciais)")
            print("7 - Aniversariantes do mês")
            print("8 - Abrir arquivo")
            print("9 - Salvar arquivo")
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
                self.pesquisar()
            elif opcao == "7":
                self.aniversariantes()
            elif opcao == "8":
                self.abrir()
            elif opcao == "9":
                self.salvar()
            elif opcao == "0":
                print("Encerrando programa.")
                break
            else:
                print("Opção inválida.")

    def inserir(self):
        id = input("ID: ")
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        if id in self.contatos:
            print("ID já existe.")
        else:
            contato = Contato(id, nome, email, telefone, nascimento)
            self.contatos[id] = contato
            print("Contato cadastrado com sucesso.")

    def listar(self):
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        else:
            for contato in self.contatos.values():
                print(contato.ToString())

    def listar_id(self):
        id = input("Digite o ID: ")
        if id in self.contatos:
            print(self.contatos[id].ToString())
        else:
            print("Contato não encontrado.")

    def atualizar(self):
        id = input("ID do contato para atualizar: ")
        if id in self.contatos:
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            telefone = input("Novo telefone: ")
            nascimento = input("Nova data de nascimento (DD/MM/AAAA): ")
            contato = self.contatos[id]
            contato.set_nome(nome)
            contato.set_email(email)
            contato.set_telefone(telefone)
            contato.set_nascimento(nascimento)
            print("Contato atualizado com sucesso.")
        else:
            print("Contato não encontrado.")

    def excluir(self):
        id = input("ID do contato a excluir: ")
        if id in self.contatos:
            del self.contatos[id]
            print("Contato excluído com sucesso.")
        else:
            print("Contato não encontrado.")

    def pesquisar(self):
        trecho = input("Digite o início do nome: ").lower()
        encontrados = [c for c in self.contatos.values() if c.get_nome().lower().startswith(trecho)]
        if encontrados:
            for c in encontrados:
                print(c.ToString())
        else:
            print("Nenhum contato encontrado com essas iniciais.")

    def aniversariantes(self):
        mes = input("Digite o mês (ex: 01 para janeiro): ")
        encontrados = []
        for contato in self.contatos.values():
            nascimento = contato.get_nascimento()
            if len(nascimento) >= 5 and nascimento[3:5] == mes:
                encontrados.append(contato)
        if encontrados:
            for c in encontrados:
                print(c.ToString())
        else:
            print("Nenhum aniversariante neste mês.")

    def abrir(self):
        try:
            with open("contatos.json", "r") as f:
                dados = json.load(f)
                self.contatos = {}
                for id, c in dados.items():
                    contato = Contato(c["_id"], c["_nome"], c["_email"], c["_telefone"], c["_nascimento"])
                    self.contatos[id] = contato
            print("Contatos carregados do arquivo.")
        except:
            print("Erro ao abrir o arquivo ou arquivo não existe.")

    def salvar(self):
        dados = {}
        for id, contato in self.contatos.items():
            dados[id] = contato.__dict__
        with open("contatos.json", "w") as f:
            json.dump(dados, f, indent=4)
        print("Contatos salvos no arquivo.")

if __name__ == "__main__":
    app = ContatoUI()
    app.menu()