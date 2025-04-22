n = int(input())
if n > 0:
    if n % 2 == 0:
        print("PAR POSITIVO")
    else:
        print("IMPAR POSITIVO")
elif n < 0:
    if n % 2 == 0:
        print("PAR NEGATIVO")
    else:
        print("IMPAR NEGATIVO")