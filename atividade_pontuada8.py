import os

# limpando o terminal


os.system ("cls || clear")

# Ler a cor do CD

cor = input("Digite a cor do CD (verde, azul, amarelo ou vermelho): ").lower()

# Verificar o preço de acordo com a cor

if cor == "verde":
    preco = 10
elif cor == "azul":
    preco = 20
elif cor == "amarelo":
    preco = 30
elif cor == "vermelho":
    preco = 40
else:
    preco = None

# Mostrar resultado

if preco is not None:
    print("O preço do CD é: R$", preco)
else:
    print("Cor inválida.")
    
    
print("\n fim do programa")


#danterks