senha_correta = 2412
senha = int(input())
while senha != senha_correta:
    print("Senha Invalida")
    senha = int(input()) 
print("Acesso Permitido")