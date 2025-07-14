from datetime import datetime

class Boleto:
    def __init__(self, codigo, data_emissao, data_vencimento, valor_total):
        self.codigo = codigo
        self.data_emissao = datetime.strptime(data_emissao, "%d/%m/%Y")
        self.data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
        self.valor_total = valor_total
        self.valor_pago = 0.0

    def pagar(self, valor):
        self.valor_pago += valor

    def situacao(self):
        if self.valor_pago == 0:
            return "Em Aberto"
        elif self.valor_pago < self.valor_total:
            return "Pago Parcial"
        else:
            return "Pago"

    def mostrar_dados(self):
        return f"Código: {self.codigo}\nEmissão: {self.data_emissao.strftime('%d/%m/%Y')}\n" + \
               f"Vencimento: {self.data_vencimento.strftime('%d/%m/%Y')}\n" + \
               f"Valor Total: R$ {self.valor_total:.2f}\nValor Pago: R$ {self.valor_pago:.2f}\n" + \
               f"Situação: {self.situacao()}"

print("Cadastro de Boleto")
codigo = input("Código de Barras: ")
data_emissao = input("Data de emissão (dd/mm/aaaa): ")
data_vencimento = input("Data de vencimento (dd/mm/aaaa): ")
valor_total = float(input("Valor total: R$ "))

boleto = Boleto(codigo, data_emissao, data_vencimento, valor_total)

valor_pago = float(input("Valor pago agora: R$ "))
boleto.pagar(valor_pago)

print("\nDados do boleto:")
print(boleto.mostrar_dados())