s = input("Digite uma frase:\n")
for _ in range(len(s)):
    s = s[1:] + s[0]
    print(s)