def maior (x,y):
    if x > y:
        return x
    else:
        return y
        def main():
                x = float(input("informe o primeiro número"))
                y = float(input("informe o segundo numero"))
                resultado = maior(x,y)
                print(f"o valor maior entre {x} e {y} é {resultado}")
                main()