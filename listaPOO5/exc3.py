from datetime import datetime

class Contato:
    def __init__(self, id, nome, email, telefone, nascimento):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

    def mostrar(self):
        return f"ID: {self.id}\nNome: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}\nNascimento: {self.nascimento.strftime('%d/%m/%Y')}"

contatos = []

def inserir():
    print("Novo Contato")
    id = input("ID: ")
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    nascimento = input("Nascimento (dd/mm/aaaa): ")
    novo = Contato(id, nome, email, telefone, nascimento)
    contatos.append(novo)
    print("Contato adicionado!")

def listar():
    print("\n--- Lista de Contatos ---")
    for contato in contatos:
        print(contato.mostrar())
       3
    

def atualizar():
    id_busca = input("ID do contato a atualizar: ")
    for contato in contatos:
        if contato.id == id_busca:
            contato.nome = input("Novo nome: ")
            contato.email = input("Novo email: ")
            contato.telefone = input("Novo telefone: ")
            nascimento = input("Nova data nascimento (dd/mm/aaaa): ")
            contato.nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
            print("Atualizado!")
            return
    print("Contato não encontrado!")

def excluir():
    id_busca = input("ID do contato a excluir: ")
    for contato in contatos:
        if contato.id == id_busca:
            contatos.remove(contato)
            print("Contato removido!")
            return
    print("Contato não encontrado!")

def pesquisar():
    letra = input("Digite as iniciais do nome: ").lower()
    for contato in contatos:
        if contato.nome.lower().startswith(letra):
            print(contato.mostrar())
            print("------------------------")

def aniversariantes():
    mes = int(input("Digite o mês (1-12): "))
    for contato in contatos:
        if contato.nascimento.month == mes:
            print(contato.mostrar())
            print("------------------------")

def menu():
    while True:
        print("\nMenu da Agenda")
        print("1 - Inserir Contato")
        print("2 - Listar Contatos")
        print("3 - Atualizar Contato")
        print("4 - Excluir Contato")
        print("5 - Pesquisar por nome")
        print("6 - Mostrar aniversariantes do mês")
        print("0 - Sair")
        op = input("Escolha: ")

        if op == "1":
            inserir()
        elif op == "2":
            listar()
        elif op == "3":
            atualizar()
        elif op == "4":
            excluir()
        elif op == "5":
            pesquisar()
        elif op == "6":
            aniversariantes()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()