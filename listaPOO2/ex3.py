class conta:
    def __init__(self):
        self._titular = ""
        self._numero = ""
        self._saldo = "0"
    def set_titular (self, t):
        if t == "": raise ValueError()
        self.__titular = t
    def get_titular(self):
        return self.__titular
    def get_saldo(self):
        return self.__saldo
    def depositar(self, V):
        if V < 0: raise ValueError()
        self.__saldo += V
    def sacar(self, V):
        if V < 0 : raise ValueError()
        if V > self.__saldo: raise ValueError()
        self__salto -= V
    class UI:
        @staticmethod
        def main():
            x = conta()
            x.set_titular(input())
            x.set_numero(input())
            x.depositar(float(input()))
            print(f"Você tem {x.get_saldo()}")
    UI.main()