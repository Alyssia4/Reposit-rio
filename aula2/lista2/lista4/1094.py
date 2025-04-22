total_experimentos = int(input())
ratos = 0
sapos = 0
coelhos = 0

for _ in range(total_experimentos):
    tipo, quantidade = input().split()  
    tipo = int(tipo)  
    quantidade = int(quantidade) 

    if tipo == 1:
        ratos += quantidade
    elif tipo == 2:
        sapos += quantidade
    elif tipo == 3:
        coelhos += quantidade
total_animais = ratos + sapos + coelhos
if total_animais > 0:
    percent_ratos = (ratos / total_animais) * 100
    percent_sapos = (sapos / total_animais) * 100
    percent_coelhos = (coelhos / total_animais) * 100
    print(f"Percentual de Ratos: {percent_ratos:.2f} %")
    print(f"Percentual de Sapos: {percent_sapos:.2f} %")
    print(f"Percentual de Coelhos: {percent_coelhos:.2f} %")
else:
    print("Nenhum animal registrado.")