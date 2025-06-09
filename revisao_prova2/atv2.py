class pais:
    def __init__(self, nome, população, área):
        self._nome = nome
        self._população = população
        self._área = área
    def set_nome(self, nome):
        if nome < 0: raise ValueError()
        self._nome = nome
    def get_nome(self):
        return self._nome
    def set_população(self, p):
        if p < 0: raise ValueError()
        self._população = p
    def get_população(self):
        return self._população
    def set_área(self, a):
        if a < 0: raise ValueError()
        self._área = a
    def get_área(self):
        return self._área
    def densidade(self):
        return self._população / self._área
    
class ParcialUI:
    @staticmethod
    def menu():
        print("\nMenu:")
        print("1- Calcular:")
        print("2- Fim:")
        opcao = input("Escolha uma opção:")
        return opcao
    @staticmethod
    def calculo():
        nome = input("informe o nome:")
        populacao = float(input("informe a população:"))
        área = float(input("informe a área (km²):"))

        pais_obj = pais(nome, populacao, área)

        print("\n dados do pais")
        print(f"nome {pais_obj.get_nome()}")
        print(f"populacao {pais_obj.get_população():,.0f} habitantes")
        print(f"área {pais_obj.get_área():,.2f} km²")
        print(f"densidade {pais_obj.densidade():.2f} hab/km²")
    @staticmethod
    def main():
        while True:
            opcao = ParcialUI.menu()
            if opcao == "1":
                ParcialUI.calculo()
            elif opcao == "2":
                print("Fim")
                break
            else:
                print("Opção inválida.")

ParcialUI.main()