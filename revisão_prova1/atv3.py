print("Escreva uma frase")
s = input()
for k in range(0, len(s), 2):
    print(s[k], end="")
print()