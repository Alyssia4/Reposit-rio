import math
class circulo:
    def __init__(self):
        self._raio = 0.0
    def set_raio(self, r):
        if r < 0: raise ValueError()
        self._raio = r
    def get_raio(self):
        return self._raio
    def area(self):
        return math.pi * (self._raio ** 2)
    def circunferencia(self):
        return 2 * math.pi * self._raio
    
class UI:
    @staticmethod
    def main():
        c = circulo()
        r = float(input("Digite o raio do círculo: "))
        c.set_raio(r)
        print(f"Raio: {c.get_raio()}")
        print(f"Área: {c.area():.2f}")
        print(f"Circunferência: {c.circunferencia():.2f}")
UI.main()