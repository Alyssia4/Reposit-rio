class ingresso:
    def __init__(self):
        self.dia = "Dom"
        self.hora = 18
    def entrada_inteira(self):
        if self.dia == "qua": return 8
        valor = 16
        if self.dia == "sex" or self.dia == "sab" or self.dia =="dom": valor = 20
        if self.hora == 0 or self.hora >= 17: valor = 1.5 * valor
        return valor
    def meia_entrada(self):
        if self.dia == "qua": return 8
        return self.entrada_inteira() / 2
    
x = ingresso()
print(x.dia, x.hora)
print(x.entrada_inteira())
print(x.meia_entrada())

y = ingresso()
y.dia = "sab"
y.hora = 15
print(y.dia, y.hora)
print(y.entrada_inteira())
print(y.meia_entrada())

z = ingresso()
z.dia = "seg"
z.hora = 0
print(z.dia, z.hora)
print(z.entrada_inteira())
print(z.meia_entrada())