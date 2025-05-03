class ContaBancaria:
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

# testando código

titular = input("Nome do titular:")
numero = input("Número da conta:")
conta = ContaBancaria(titular, numero)

conta.depositar(float(input("Valor para depósito: ")))
conta.sacar(float(input("Valor para saque: ")))
conta.mostrar_saldo()