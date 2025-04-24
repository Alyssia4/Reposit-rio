s = input("Digite uma frase:\n").lower()
for v in "aeiou":
    print(f"{v.upper()} – {s.count(v)}")