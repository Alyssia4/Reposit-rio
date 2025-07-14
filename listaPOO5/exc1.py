from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

    def idade(self):
        hoje = datetime.today()
        anos = hoje.year - self.nascimento.year
        meses = hoje.month - self.nascimento.month
        if hoje.day < self.nascimento.day:
            meses -= 1
        if meses < 0:
            anos -= 1
            meses += 12
        return f"{anos} anos e {meses} meses"

    def mostrar_dados(self):
        nasc = self.nascimento.strftime("%d/%m/%Y")
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.telefone}\nNascimento: {nasc}"


print("Cadastro de Paciente")
nome = input("Nome: ")
cpf = input("CPF: ")
telefone = input("Telefone: ")
nascimento = input("Data de nascimento (dd/mm/aaaa): ")

p = Paciente(nome, cpf, telefone, nascimento)
print("\nDados do paciente:")
print(p.mostrar_dados())
print("Idade:", p.idade())